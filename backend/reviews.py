from flask import (
    Blueprint, g, request, jsonify
)

from backend.auth import login_required
from backend.db import get_db

bp = Blueprint('reviews',__name__)


@bp.route('/book/<int:book_id>/view_reviews')
def view_reviews(book_id):
    db = get_db()
    reviews = db.execute(
        '''SELECT reviews.*,users.username FROM reviews JOIN users ON reviews.reviewer = users.userID WHERE reviews.book = ?''',
        (book_id,)
    ).fetchall()
    return jsonify([dict(row) for row in reviews])

@bp.route('/book/<int:book_id>/view_user_review')
@login_required
def view_user_review(book_id):
    db = get_db()
    print(g.user)
    user_id = g.user
    review = db.execute(
        '''SELECT * FROM reviews WHERE book = ? AND reviewer = ?''',
        (book_id,user_id)
    ).fetchone()
    if not review:
        return jsonify({"error": "Review not found"}),404
    return jsonify(dict(review))

@bp.route('/book/<int:book_id>/make_review',methods=['POST'])
@login_required
def review(book_id):
    db = get_db()
    user_id = g.user
    rating = request.form['rating']
    comment = request.form['user_Review']
    read_status = request.form['read_status']
    start_read = request.form['start_read']
    finish_read = request.form['finish_read']
    if not start_read:
        start_read = None
    if not finish_read:
        finish_read = None

    error = None
    if not rating:
        error = 'Rating is required'
    elif not comment:
        error = 'Comment is required'
    elif len(comment)>=1000:
        error = 'Comment is too long'

    if error is not None:
        return jsonify({"error": error}),400
    
    db.execute(
        '''DELETE FROM reviews WHERE book = ? AND reviewer = ?''',
        (book_id, user_id)
    )
    db.execute(
        '''INSERT INTO reviews (book, reviewer, rating, user_Review, read_status, start_read, finish_read)
        VALUES (?,?,?,?,?,?,?)''',
        (book_id, user_id, rating, comment, read_status, start_read, finish_read)
    )
    db.commit()
    return jsonify({"message": "Review added successfully"}),201

@bp.route('/user/<int:user_id>/review',methods=['GET'])
def user_review(user_id):
    db = get_db()
    reviews = db.execute(
        '''SELECT reviews.*, books.title
        FROM reviews JOIN books
        ON reviews.book = books.bookID
        WHERE reviews.reviewer = ?''',
        (user_id,)
    ).fetchall()
    return jsonify([dict(row) for row in reviews])

@bp.route('/book/<int:book_id>/delete_review',methods=['DELETE'])
@login_required
def delete_review(book_id):
    db = get_db()
    user_id = g.user
    db.execute(
        '''DELETE FROM reviews WHERE book = ? AND reviewer = ?''',
        (book_id,user_id)
    )
    db.commit()
    return jsonify({"message": "Review deleted successfully"}),200