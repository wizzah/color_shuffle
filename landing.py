from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import extract_gif
import process
import stitch
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['GET', 'POST'])
def img_upload():
    if request.method == 'POST':
        gif = request.files["uploaded"]
        extract_gif.extract_gif(gif)
        process.process_gif()
        result = stitch.stitch()
        return send_file(result, 'image/gif')

