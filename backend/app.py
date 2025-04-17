from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
import your_resume_matching_module  # replace with actual model import

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_files():
    jd_file = request.files.get('jd')
    cvs_files = request.files.getlist('cvs')

    if not jd_file or not cvs_files:
        return jsonify({'error': 'JD or CV files missing'}), 400

    jd_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(jd_file.filename))
    jd_file.save(jd_path)

    cv_paths = []
    for file in cvs_files:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        cv_paths.append(filepath)

    # Call your resume matching model here
    results = your_resume_matching_module.match(jd_path, cv_paths)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
