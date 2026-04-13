from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Image folder
IMAGE_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# Auto create folder if not exists
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# Home (Gallery)
@app.route('/')
def index():
    images = os.listdir(IMAGE_FOLDER)
    return render_template('index.html', images=images)

# Upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist('images')

        for file in files:
            if file:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return redirect(url_for('index'))

    return render_template('upload.html')

# Delete Image
@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)