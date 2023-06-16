from flask import Blueprint,request,url_for,redirect
#
blueprint_main = Blueprint(
    'main',
    __name__,
)
#
@blueprint_main.route('/')
def index():
    return redirect(url_for('localisation.home'))