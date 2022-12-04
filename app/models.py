from . import db
from dataclasses import dataclass


class Role(db.Model):
    """
    different types of rol: admin, user, mantainer
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    """
    users model with username and role_id by default
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@dataclass
class Bookmark:
    name: str
    url: str


@dataclass
class Directories:
    """
    creates a directory object with the next attributes...
    """
    name: str
    url: str
    content: str
    bookmark_type: str
    have_direct_directories: bool
    have_direct_links: bool
