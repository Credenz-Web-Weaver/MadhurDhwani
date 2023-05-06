from flask import Flask, Response, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename

# creating app instance 
app = Flask(__name__)

# folder to store uploaded files
UPLOAD_FOLDER = 'static/uploads'

app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH']

filename = ""

# audio formats 
ALLOWED_EXTENSIONS = set(["mp3" , "mp4" , "mpeg" , "mpga" , "m4a" , "wav" , "webm"])

def allowed_filename(filename) :
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/hello")
def hello() :
    return render_template("index.html")

@app.route("/")
# @app.route("/home")
def home() :
    return render_template("index.html")

@app.route("/", methods=("GET","POST"))
def upload() :

    if 'file' not in request.files :
        flash("No file part")
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "" :
        flash("No file selected for uploading")
        return redirect(request.url)
    


    if file and allowed_filename(file.filename) :
        filename = secure_filename(file.filename)
        # url = os.getcwd() + os.path.join("\static","uploads",f"{filename}")
        url = f"http://127.0.0.1:5000/static/uploads/{filename}"
        print(f"""
            -------------------------
            -------------------------
            print
            -------------------------
            print
            -------------------------
            {str(url_for('static', filename = f"uploads/{filename}"))}
            -------------------------
        """)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        result = {
            "filename" : filename,
            "url" : url
        }
        flash("file uploaded successfully")
        return render_template("index.html", filename=filename, url = url)
    
    else :
        flash("Allowed file types are - " , " ".join(list(allowed_filename)))
        return redirect(request.url)
    


@app.route("/mp3/<filename>")
def stream_mp3(filename):
    def generate():
        with open(f"static/uploads/{filename}", "rb") as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    return Response(generate(), mimetype="audio/mp3")

@app.route("/display/<filename>")
def display_image(filename) :
    name = filename.split(".")[0]
    print("--------------\n\n --------------")
    url = str(url_for('static', filename = f"uploads/{filename}"))
    flash(str(url))
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__" :
    app.run()