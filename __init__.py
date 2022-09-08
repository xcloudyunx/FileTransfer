import os
from flask import Flask, render_template, request, flash, redirect, send_from_directory
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config["UPLOAD_FOLDER"] = "./FileTransfer/uploads"
    app.config["SECRET_KEY"] = os.urandom(12).hex()

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            file = request.files["file"]
            if file.filename == '':
                flash("No selected file")
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return render_template("index.html")
    
    @app.route('/uploads/<name>')
    def download_file(name):
        return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    
    
    return app