from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'todo.db'

def buat_tabel():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tugas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teks_tugas TEXT,
            selesai INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tugas', methods=['GET'])
def ambil_tugas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tugas')
    data = cursor.fetchall()
    conn.close()
    
    hasil = []
    for row in data:
        hasil.append({
            'id': row[0],
            'teks_tugas': row[1],
            'selesai': row[2]
        })
    return jsonify(hasil)

@app.route('/api/tugas', methods=['POST'])
def tambah_tugas():
    data = request.get_json()
    teks = data.get('teks_tugas')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tugas (teks_tugas) VALUES (?)', (teks,))
    conn.commit()
    conn.close()
    
    return jsonify({'pesan': 'Tugas berhasil ditambah'})

@app.route('/api/tugas/<int:id>', methods=['PUT'])
def update_tugas(id):
    data = request.get_json()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if 'selesai' in data:
        cursor.execute('UPDATE tugas SET selesai = ? WHERE id = ?', (data['selesai'], id))
    if 'teks_tugas' in data:
        cursor.execute('UPDATE tugas SET teks_tugas = ? WHERE id = ?', (data['teks_tugas'], id))
        
    conn.commit()
    conn.close()
    return jsonify({'pesan': 'Tugas diupdate'})

@app.route('/api/tugas/<int:id>', methods=['DELETE'])
def hapus_tugas(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tugas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'pesan': 'Tugas dihapus'})

if __name__ == '__main__':
    buat_tabel()
    app.run(debug=True)