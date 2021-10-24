import os

from flask import Flask, render_template, url_for, redirect, request

from pm import import_csv

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
LOGS_FOLDER = 'static\\logs'
app.config['LOGS_FOLDER'] = LOGS_FOLDER


@app.route("/")
def index():
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def upload_files():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename.__contains__(".csv"):
        print(uploaded_file.filename)
        print(type(uploaded_file))

        file_path = os.path.join(app.config['LOGS_FOLDER'], uploaded_file.filename)
        print("File path:", file_path)

        uploaded_file.save(file_path)

        import_csv(file_path)

    return redirect(url_for('index'))
