"""SQLAlchemy models and utility functions for TwitOff."""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users corresponding to Tweets."""
    
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    
    def __repr__(self):
        return '-User {}-'.format(self.name)
    
class Tweet(DB.Model):
    """Tweet text and data."""
    
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for text + links
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    
    def __repr__(self):
        return '-Tweet {}-'.format(self.text)
    
def insert_example_users():
    """Example data to play with."""
    austen = User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    dondre = User(id=3, name='dondre')
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.add(dondre)
    DB.session.commit()
    
def insert_example_tweets():
    """Example data to play with."""
    austen_tweet = Tweet(id=1, 
                          text='I am Austen!',
                          user='austen')
    austen_tweet2 = Tweet(id=1, 
                        text='How Awesome is Lambda?!! (:',
                        user='austen')
    elon_tweet = Tweet(id=2, 
                          text='I am Elon!',
                          user='elon')
    elon_tweet2 = Tweet(id=2, 
                        text='How about that SpaceX?! ;)',
                        user='elon')
    dondre_tweet = Tweet(id=3, 
                        text="I am Dondre'",
                        user='dondre')
    dondre_tweet2 = Tweet(id=3, 
                          text="""I wish my bed was as comfortable 
                          when I try to sleep as it is when my alarm goes off...""",
                          user='dondre')
    
    DB.session.add(austen_tweet)
    DB.session.add(austen_tweet2)
    DB.session.add(elon_tweet)
    DB.session.add(elon_tweet2)
    DB.session.add(dondre_tweet)
    DB.session.add(dondre_tweet2)
    DB.session.commit()