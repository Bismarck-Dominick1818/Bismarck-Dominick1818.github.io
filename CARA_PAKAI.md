# Cara Pakai Blog Ini

## Yang ada di folder ini
- `index.html` -> halaman website blog kamu
- `posts.json` -> data tulisan (dibaca otomatis oleh index.html)
- `fetch_notion.py` -> script untuk mengambil tulisan terbaru dari Notion

## Setup awal (sekali saja)

1. Pastikan Python sudah terinstall di komputermu.
   Cek dengan membuka Terminal (Mac) atau Command Prompt (Windows), lalu ketik:
   ```
   python3 --version
   ```
   Kalau belum ada, download di https://www.python.org/downloads/

2. Buka file `fetch_notion.py` dengan text editor (Notepad, TextEdit, atau VS Code).

3. Ganti baris ini dengan token dan database ID kamu dari Notion:
   ```python
   NOTION_TOKEN = "TEMPEL_TOKEN_NOTION_DI_SINI"
   DATABASE_ID = "TEMPEL_DATABASE_ID_DI_SINI"
   ```
   Simpan filenya.

## Setiap kali ada tulisan baru di Notion

1. Tulis dan publish tulisan barumu di Notion (centang kolom "Published").

2. Buka Terminal / Command Prompt, masuk ke folder ini, lalu jalankan:
   ```
   python3 fetch_notion.py
   ```
   Ini akan memperbarui file `posts.json` dengan tulisan terbaru.

3. Upload ulang file `posts.json` ke GitHub:
   - Buka repository GitHub kamu di browser
   - Klik file `posts.json` -> klik ikon pensil (Edit)
   - Hapus semua isi lama, lalu tempel (paste) isi baru dari file posts.json di komputermu
   - Scroll ke bawah, klik "Commit changes"

4. Tunggu 1-2 menit, lalu buka website kamu di `https://username-kamu.github.io` -- tulisan baru akan muncul!

## Troubleshooting

- **Error "Gagal mengambil data dari Notion"**: cek lagi apakah token sudah benar dan database sudah di-connect ke integration/connection di Notion (lihat menu ... di database -> Add connections).
- **Website kosong / tidak ada tulisan**: pastikan kolom "Published" di Notion sudah dicentang untuk tulisan yang ingin ditampilkan.
- **Website tidak update setelah upload**: tunggu sebentar (GitHub Pages butuh waktu build), lalu refresh browser dengan Ctrl+Shift+R (hard refresh).
