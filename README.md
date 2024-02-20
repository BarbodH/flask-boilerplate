# Flask Boilerplate

This repository is a basic project structure and configuration setup for a Flask application.
It provides a starting point for developing Flask-based web applications.

## Usage

- Clone the repository:
```shell
git clone https://github.com/BarbodH/flask-boilerplate.git
```
- Install dependencies:
```shell
pip install -r requirements.txt
```
- Set up your virtual environment (optional but recommended).
- Customize configuration:
  - Create a `config.json` file in the project root to adjust application settings as needed for development, production, and testing environments.
  - Add sensitive information such as database credentials or secret key to environment variables.
```json
{
  "PORT": 5000,
  "DEBUG": true,
  "SECRET_KEY": "your_secret_key",
  "DATABASE": {
    "HOST": "localhost",
    "USERNAME": "your_username",
    "PASSWORD": "your_password",
    "PORT": 3306,
    "NAME": "your_database_name"
  }
}
```
- Run the application:
```shell
python app.py
```

## License
This project is licensed under the [MIT License](LICENSE).
