# Slot-Hybrid

Slot-Hybrid adalah sebuah bot yang berfungsi untuk melakukan transaksi otomatis pada jaringan blockchain Hybrid. Bot ini secara otomatis menjalankan dua jenis transaksi: `mint` untuk minting token baru dan `spin` untuk transaksi lainnya. Transaksi `mint` dilakukan setiap 20 kali transaksi `spin` berhasil.

## Fitur

- **Transaksi Otomatis:** Bot ini dapat menjalankan transaksi `mint` dan `spin` secara otomatis.
- **Pengelolaan Nonce:** Menangani nonce transaksi secara dinamis untuk menghindari kesalahan "nonce too low".
- **Penundaan Transaksi:** Setiap transaksi memiliki jeda waktu 5 detik untuk menghindari penumpukan transaksi.
- **ASCII Art:** Menampilkan ASCII art pada bagian atas terminal sebagai hiasan visual.

## Instalasi

1. Clone repository ini ke lokal Anda:
   
 ```bash
 git clone https://github.com/vinskasenda/Slot-Hybrid.git
```

2. Masuk Direktori

```bash
cd Slot-Hybrid
```
3. Install Web3 dan termcolor

```bash
pip install web3 termcolor
```

4. Atur Konfigurasi di dalam file

```bash
nano Slot.py
```

5. Ganti Private Key dan My Address (EVM)

6. Jalankan Bot

```bash
python Slot.py
```

## Kontribusi
Jika Anda menemukan bug atau ingin menambahkan fitur baru, jangan ragu untuk membuka issue atau pull request.

## Lisensi
