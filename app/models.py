from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.String(255))
    email = db.Column(db.String(80), unique=True)
    age = db.Column(db.String(3))
    gender = db.Column(db.String(1))
    profile_image = db.Column(db.String(255))
    wishlist = db.relationship('Wishlist', backref='user', uselist=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('ListItem', backref='wishlist', lazy='dynamic')

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

class ListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1100))
    website_address = db.Column(db.String(250))
    thumbnail_image = db.Column(db.String(250))
    price = db.Column(db.String(20))
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
