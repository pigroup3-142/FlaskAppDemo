from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return render_template("index.html")

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

def handle(path_file):
	return path_file

@app.route("/", methods=["POST"])
def uploader():
	if request.method == "POST" :
		file = request.files["file"]
		if file.filename == "":
			return redirect(request.url)

		file_name = file.filename
		create_new_folder(app.config['UPLOAD_FOLDER'])
		saved_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
		file.save(saved_path)
		return handle(saved_path)

	return "404 NOT FOUND"

if __name__ == "__main__":
    app.run(debug = True)