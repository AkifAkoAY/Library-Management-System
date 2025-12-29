📚 Library-Management-System

Bu proje, SQLite veritabanı kullanan bir Komut Satırı (CLI) tabanlı Kütüphane Yönetim Sistemi’dir.
Kullanıcılar kitap ekleme, listeleme, silme, güncelleme ve arama işlemlerini kolayca gerçekleştirebilir.

📝 Proje Dosyası

Ana Python Dosyası: LibraryDataBase.py

Veritabanı Dosyası: library.db (Program çalıştığında otomatik oluşturulur)

✨ Özellikler

✔️ SQLite ile kalıcı veri saklama

✔️ Kitap ekleme

✔️ Kitap listeleme

✔️ Kitap silme

✔️ Kitap güncelleme

✔️ Başlık, yazar veya yayın yılına göre arama

✔️ Giriş kontrolleri ve hata yakalama

🛠️ Kullanılan Teknolojiler

Python 3

SQLite (sqlite3 kütüphanesi)
Ekstra paket kurulumuna gerek yoktur.

📥 Kurulum

Projeyi indirin:

cd Library-Management-System


Çalıştırmak için:

python LibraryDataBase.py

▶️ Kullanım

Program açıldığında aşağıdaki menü görünür:

=== MENU ===
1. Kitap Ekle
2. Kitaplari Listele
3. Kitap Sil
4. Kitap Guncelle
5. Kitap Ara
6. Cikis


Her seçenek ilgili işlemi yapmanızı sağlar.

🗂️ Veritabanı Yapısı
Alan	Tip
id	INTEGER PRIMARY KEY AUTOINCREMENT
title	TEXT
author	TEXT
year_published	INTEGER
