# Woven Pages
- The Project is a Book Cataloguing system that helps users discover, review, and track books.
- Users can Track what they read, and view statistics about their reading habits.
- Users can review books and discover books based on reviews of other similar users.

## Installation and Setup

1. Download and install [Python](https://docs.python.org/) and [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2. Clone this repository
    ``` bash
    git clone https://github.com/math-lover31415/DBMS-Project.git
    cd DBMS-Project
    ```

3. Create virtual environment
    ```bash
    python -m venv venv
    ```

4. Activate virtual environment
    -   Linux:
    ```bash
    source venv/bin/activate
    ```
    - Windows
    ```
    venv\Scripts\activate
    ```
5. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Create database
   ```bash
   flask init-db
   ```
7. Run flask app
    ```bash
    flask run
    ```
8. Run frontend
   ```bash
   cd frontend
   npm run dev
   ```
