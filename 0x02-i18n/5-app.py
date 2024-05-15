#!/usr/bin/env python3
'''Emulating a copy of creating a user login system with given params
'''

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''Config class that has languages'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Return user dictionary or None if not found."""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set the logged-in user as a global on flask.g.user."""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else No


@babel.localeselector
def get_locale() -> str:
    """Retrieves the best match to our supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''default route to html homepage
    '''
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
