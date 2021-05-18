from flask import Flask
from app.routes import home

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECTRET_KEY = 'super secret key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'
    #registerer routes
    app.register_blueprint(home)

    return app