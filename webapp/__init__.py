from flask import Flask, render_template
from webapp.model import db, Idioms


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def index():
        page_title = "Learn Idioms"
        return render_template('index.html', page_title=page_title)
    return app
