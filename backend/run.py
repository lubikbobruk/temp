from src import create_app, DevConfig

# Create an instance of the Flask application with the development configuration.
app = create_app(DevConfig)


if __name__ == '__main__':
    """
    Run the application.

    This is the starting point of the application. It will be used when the script is run directly from the
    command line using the "python run.py" command.
    """
    app.run()
