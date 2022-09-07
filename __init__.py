from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def index():
        return render_template(("index.html"))
    
    return app