from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulasi database sederhana menggunakan list
data_warga = []

@app.route('/')
def login_page():
    return render_template('auth.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Logika autentikasi sederhana
    if username == 'admin' and password == 'admin123':
        return redirect(url_for('input_page'))
    else:
        return "Login failed! Invalid credentials."

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    data = {
        'id': len(data_warga) + 1,
        'nama_lengkap': request.form['nama_lengkap'],
        'tanggal_lahir': request.form['tanggal_lahir'],
        'jenis_kelamin': request.form['jenis_kelamin'],
        'alamat': request.form['alamat'],
        'rt': request.form['rt'],
        'rw': request.form['rw'],
        'status_tempat_tinggal': request.form['status_tempat_tinggal']
    }

    data_warga.append(data)
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    warga = None
    # Cari data warga berdasarkan id
    for item in data_warga:
        if item.get('id') == id:  # Menggunakan .get() untuk menghindari KeyError
            warga = item
            break

    if warga is None:
        return "Warga tidak ditemukan", 404

    if request.method == 'POST':
        # Proses form edit
        # warga['id'] = len(data_warga) + 1
        warga['nama_lengkap'] = request.form['nama_lengkap']
        warga['tanggal_lahir'] = request.form['tanggal_lahir']
        warga['jenis_kelamin'] = request.form['jenis_kelamin']
        warga['alamat'] = request.form['alamat']
        warga['rt'] = request.form['rt']
        warga['rw'] = request.form['rw']
        warga['status_tempat_tinggal'] = request.form['status_tempat_tinggal']
        return redirect('/dashboard')
    
    return render_template('edit.html', warga=warga)

@app.route('/dashboard')                                                                                                                                            
def dashboard():
    return render_template('dashboard.html', data_warga=data_warga)

@app.route('/logout')
def logout():
    # Logout dan arahkan kembali ke halaman login
    return redirect(url_for('login_page'))
    
if __name__ == '__main__':
    app.run(debug=True)
