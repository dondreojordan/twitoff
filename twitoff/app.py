"""Main app/routing file for Twitoff."""
from flask import Flask, render_template
from .models import DB, User, insert_example_users, insert_example_tweets


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)  # Might have to delete file for editing.
    
    #...TODO make the app
    @app.route('/')  # Listens for a request and returns a response. Heart of routing.
    def root():
        return render_template('base.html', title='Home', 
                               users=User.query.all())
    
    @app.route('/update')
    def update():
        # Reset the Database
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        insert_example_tweets()
        return render_template('base.html', title='Users Updated',
                               users=User.query.all())

    
    return app