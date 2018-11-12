import os

from flask import Flask


def create_app(test_config=None):
    # create a new instance of the application
    app = Flask(__name__, instance_relative_config=True)

    # set absolute configuration values for all instances
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite')
    )

    # load additional configuration values from file, if it exisits
    if test_config is None:  # Default
        # load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:  # we're testing
        # load the test configuration
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # simple test page
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
