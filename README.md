Tuliskan aturan KBM: hanya gunakan lab ini untuk latihan, jangan expose ke internet, simpan catatan, dll.
Setelah Codespace siap, buka terminal.

Jalankan:

# di root repo
./run_lab.sh


Verifikasi target web jalan:

# di Codespace terminal
curl -s http://127.0.0.1:8000/ | sed -n '1,20p'
# atau buka port preview di Codespace (Ports view) untuk melihat web UI


Jalankan attacker scripts:

# scan
./attacker/scan.sh 127.0.0.1 8000

# test XSS
./attacker/test_xss.sh http://127.0.0.1:8000

# test SQLi
./attacker/test_sqli.sh http://127.0.0.1:8000


Saat selesai, hentikan target:

# hentikan
kill $(cat target.pid) && rm target.pid

13 — Catatan pengajaran (ide KBM)

Sesi 1: Pengenalan web app & konsep keamanan — buka index, jelaskan apa itu XSS, SQLi, command injection.

Sesi 2: Demonstrasi aman — jalankan test_xss.sh dan tunjukkan bagaimana payload tercermin. Diskusikan mitigasi (escaping, Content Security Policy).

Sesi 3: Demonstrasi SQLi — jalankan test_sqli.sh (query injection yang menampilkan semua users). Diskusikan parameterized queries (prepared statements) sebagai solusi.

Sesi 4 (opsional): Tugas praktis—minta siswa menambal kerentanan: ubah search() untuk menggunakan parameterized query, dan perbaiki greet() agar escape output; lalu buat test untuk membuktikan perbaikan.

14 — Keamanan & etika (harus disampaikan ke siswa)

Lab ini hanya untuk tujuan pendidikan pada mesin yang kamu kendalikan.

Jangan deploy app rentan ke internet publik.

Simpan password & hasil tugas secara privat.

Jelaskan konteks legal: eksploitasi tanpa izin adalah ilegal.
