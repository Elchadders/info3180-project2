"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from models import UserProfile
from forms import SignUpForm, LoginForm
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
import image_getter

###
# Routing for your application.
###

@app.route('/')
@login_required
def home():
    """Render website's home page."""
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="creating Wishlists")

@app.route('/api/users/register/', methods=['POST', 'GET'])
def register():
    form = SignUpForm()

    if request.method == "POST":

        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        email = request.form.get("email")
        age = request.form.get("age")
        gender = request.form.get("gender")
        password = request.form.get("password")
        password_confirm = request.form.get("passwordConfirm")

        if not password == password_confirm:
            return render_template('register.html')


        user = UserProfile(first_name=first_name, last_name=last_name, email=email, password=password, 
            age=age, gender=gender)
        db.session.add(user)
        db.session.commit()

    elif request.method == "GET":
        return render_template('register.html', form=form)

@app.route('/api/users/login/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"), code=200)
    else:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = UserProfile.query.filter_by(email=email, password=password).first()
            if user:
                login_user(user)
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
        else:
            return render_template('login.html')

@app.route('/api/users/{userid}/wishlist/', methods=['POST', 'GET'])
@login_required
def wishlist(userid):
    if request.method == 'POST':
        user = UserProfile.query.filter_by(id=userid).first()
        if user:
            title = request.form.get('title')
            description = request.form.get('description')
            website_address = request.form.get('website_address')

            wishlist = user.wishlist
        else:
            return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('wishlist.html') #Angular will make necessary request to show wishlist
    else:
        return redirect(url_for('home'))

@app.route('/api/thumbnails/', methods=['GET'])
@login_required
def thumbnails(url):
    return jsonify(error=None, message="Success", thumbnails=image_getter.get_images(url))


#need code for delete function
#using "pass" as we have not yet finished writing it
@app.route('/api/users/{userid}/wishlist/{itemid}/', methods=['DELETE'])
@login_required
def delete():
    pass

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")