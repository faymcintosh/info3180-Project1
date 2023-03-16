from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title=StringField('Property Title',validators=[DataRequired(),Length(min=1, max=160)])
    num_of_bedrooms = IntegerField('Num.of Rooms', validators=[DataRequired()])
    num_of_bathrooms=IntegerField('Num.of Bathrooms',validators=[DataRequired()])
    type_place = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')],validators=[DataRequired()])
    location=StringField('Location',validators=[DataRequired(),Length(min=1, max=70)])
    price=FloatField('Price',validators=[DataRequired()])
    description=TextAreaField('Description',validators=[DataRequired(),Length(min=1, max=360)])
    image = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])