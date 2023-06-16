from flask import Flask
#
def app_create():
    #
    from .main.controller import blueprint_main
    from .localisation.controller import blueprint_localisation
    #
    app = Flask('__name__')
    #
    app.config.from_pyfile('config.py')
    #
    app.register_blueprint(blueprint_main)
    #
    app.register_blueprint(blueprint_localisation)
    #
    return app
