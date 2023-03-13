from . import db
#from werkzeug.security import generate_password_hash


class Properties(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    #__tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(180))
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price= db.Column(db.Float)
    description= db.Column(db.String(320))
    type_place= db.Column(db.String(50))
    photo= db.Column(db.String(250))

    def  __init__(self, title, num_of_bedrooms, num_of_bathrooms, location, price, description, type_place, photo):
        self.title= title
        self.num_of_bedrooms= num_of_bedrooms
        self.num_of_bathrooms= num_of_bathrooms
        self.location= location
        self.price= price
        self.description= description
        self.type_place= type_place
        self.photo= photo

 


    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Properties %r>' % (self.title)