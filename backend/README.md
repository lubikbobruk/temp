# Movie Recommendation System

This project is a Movie Recommendation System implemented in Python using Flask, providing a REST API.

## Requirements

- Python 3.9+
- Flask
- Flask-RESTx
- Flask-JWT-Extended
- Flask-CORS
- Flask-Migrate
- SQLAlchemy

## Getting Started

1. Clone the repository:

    ```
    git clone https://gitlab.fit.cvut.cz/makardan/spearman-project
    cd spearman-project
    ```

2. (Optional) It's recommended to create a virtual environment to manage your project's dependencies:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    ```
    export FLASK_APP=run.py
    ```

5. Run database migrations:

    ```
    flask db upgrade
    ```

6. Run the Flask server:

    The application should be running at `http://localhost:5000`.

    ```
    python run.py
    ```

7. You can now interact with the API endpoints.

    The API documentation can be accessed at `http://localhost:5000/docs` - SWAGGER.