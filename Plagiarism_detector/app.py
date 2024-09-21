from flask import Flask, render_template, request, redirect, url_for
import os
import PyPDF2
import Levenshtein
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi direktori untuk mengunggah file
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fungsi untuk mengecek apakah file yang diunggah adalah PDF
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fungsi untuk membaca teks dari file PDF
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Fungsi untuk menghitung Levenshtein Distance dan kemiripan
def levenshtein_similarity(text1, text2):
    distance = Levenshtein.distance(text1, text2)
    max_len = max(len(text1), len(text2))
    similarity = (1 - distance / max_len) * 100
    return similarity

# Route utama untuk menampilkan halaman upload dan deteksi plagiarisme
@app.route('/', methods=['GET', 'POST'])
def index():
    similarity = None
    if request.method == 'POST':
        # Mengecek apakah kedua file PDF diunggah
        if 'file1' not in request.files or 'file2' not in request.files:
            return redirect(request.url)

        file1 = request.files['file1']
        file2 = request.files['file2']

        # Mengecek apakah file yang diunggah adalah PDF
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)

            # Simpan file PDF yang diunggah ke direktori upload
            path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
            file1.save(path1)
            file2.save(path2)

            # Baca teks dari kedua file PDF
            text1 = read_pdf(path1)
            text2 = read_pdf(path2)

            # Hitung kemiripan menggunakan Levenshtein
            similarity = levenshtein_similarity(text1, text2)

    return render_template('index.html', similarity=similarity)

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)