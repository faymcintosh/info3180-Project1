"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash,send_from_directory
from werkzeug.utils import secure_filename
from app.forms import Newproperty
from app.models import Properties
import os


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create',methods=['POST','GET'])
def create_properties():
    """For displaying the form to add a new property"""
    create_properties_form= PropertyForm()
    if request.method == 'POST' :
        if form.validate_on_submit():
            image =  create_properties_form.image.data 
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            create_properties=Properties(title=form.title.data, num_of_bedrooms=form.num_of_bedrooms.data,num_of_bathrooms=form.num_of_bathrooms.data,type_place=form.type_place.data,location=form.location.data,price=form.price.data
            ,description=form.description.data,photo=filename)
            db.session.add(create_properties)
            db.session.commit()
            flash('Property Saved', 'success')
            return redirect(url_for('properties'))
        else:
            flash_errors(form)
    return render_template('Newproperty.html',form=create_properties_form) 

@app.route('/properties')
def properties():
    return render_template('properties.html', properties = Properties.query.all() )

@app.route('/property/<propertyid>')
def get_property(propertyid):
    property_id = Properties.query.filter_by(id=propertyid).first()
    return render_template('property.html', property=property_id)


@app.route('/properties/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']), filename)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
