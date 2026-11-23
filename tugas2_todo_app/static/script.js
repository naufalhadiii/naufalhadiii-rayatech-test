const urlApi = '/api/tugas';

document.addEventListener('DOMContentLoaded', function() {
    tampilkanTugas();
});

function tampilkanTugas() {
    fetch(urlApi)
    .then(response => response.json())
    .then(data => {
        let list = document.getElementById('daftarTugas');
        list.innerHTML = ''; 

        for (let i = 0; i < data.length; i++) {
            let tugas = data[i];
            let classSelesai = tugas.selesai == 1 ? 'selesai' : '';
            let checked = tugas.selesai == 1 ? 'checked' : '';

            let li = document.createElement('li');
            li.className = classSelesai;
            
            li.innerHTML = `
                <input type="checkbox" ${checked} onclick="ubahStatus(${tugas.id}, ${tugas.selesai})">
                <span>${tugas.teks_tugas}</span>
                <div>
                    <button class="btn-edit" onclick="editTugas(${tugas.id}, this)">Edit</button>
                    <button class="btn-hapus" onclick="hapusTugas(${tugas.id})">Hapus</button>
                </div>
            `;
            list.appendChild(li);
        }
    });
}

function tambah() {
    let input = document.getElementById('inputTugas');
    let teks = input.value;

    if (teks == "") {
        alert("Tugas tidak boleh kosong!");
        return;
    }

    fetch(urlApi, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ teks_tugas: teks })
    })
    .then(() => {
        input.value = ''; 
        tampilkanTugas();
    });
}

function ubahStatus(id, statusSekarang) {
    let statusBaru = statusSekarang == 1 ? 0 : 1;
    fetch(urlApi + '/' + id, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ selesai: statusBaru })
    })
    .then(() => tampilkanTugas());
}

function editTugas(id, tombolEdit) {
    let li = tombolEdit.parentElement.parentElement;
    let span = li.querySelector('span');
    let teksLama = span.innerText;

    // Ubah teks jadi kotak input
    span.innerHTML = `<input type="text" id="edit-input-${id}" value="${teksLama}" style="padding: 4px; width: 70%;">`;
    
    // Ubah tombol Edit jadi Simpan
    tombolEdit.innerText = "Simpan";
    tombolEdit.className = "btn-simpan"; 
    
    // Ganti aksi tombol jadi simpan perubahan
    tombolEdit.onclick = function() {
        let teksBaru = document.getElementById('edit-input-' + id).value;
        
        if (teksBaru == "") {
            alert("Tugas tidak boleh kosong!");
            return;
        }

        fetch(urlApi + '/' + id, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ teks_tugas: teksBaru })
        })
        .then(() => tampilkanTugas());
    };
}

function hapusTugas(id) {
    let yakin = confirm("Yakin mau hapus tugas ini?");
    if (yakin) {
        fetch(urlApi + '/' + id, {
            method: 'DELETE'
        })
        .then(() => tampilkanTugas());
    }
}