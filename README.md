📚 Library Management System
Bu proje, Python ve SQLite kullanılarak geliştirilmiş, komut satırı üzerinden çalışan basit ve etkili bir Kütüphane Yönetim Sistemi'dir. Kullanıcıların kitap bilgilerini bir veritabanında saklamasına, listelemesine, güncellemesine ve silmesine olanak tanır.

✨ Özellikler
Kitap Ekleme: Kitap adı, yazar ve yayın yılı bilgilerini kaydeder.

Kitap Listeleme: Veritabanındaki tüm kitapları düzenli bir tablo formatında görüntüler.

Kitap Güncelleme: Mevcut kitapların bilgilerini ID numarası üzerinden değiştirir.

Kitap Silme: İstenilen kitabı ID numarası ile veritabanından kalıcı olarak kaldırır.

Hata Yönetimi: Geçersiz veri girişlerine (boş isim, yanlış yıl formatı vb.) karşı koruma sağlar.

🛠 Kullanılan Teknolojiler
Dil: Python 3.x

Veritabanı: SQLite3 (Gömülü veritabanı olduğu için ek bir kurulum gerektirmez)

🚀 Kurulum ve Çalıştırma
Projeyi Klonlayın:

Bash

git clone https://github.com/kullanici_adiniz/Library-Management-System.git
cd Library-Management-System
Programı Çalıştırın:

Bash

python main.py
(Dosya isminiz farklıysa main.py kısmını güncelleyin)

📂 Dosya Yapısı
main.py: Uygulamanın tüm mantığını ve veritabanı işlemlerini içeren ana dosya.

library.db: Uygulama ilk kez çalıştırıldığında otomatik olarak oluşturulan veritabanı dosyası.

📝 Kullanım Notları
Program başlatıldığında karşınıza bir menü çıkacaktır:

Kitap eklemek için 1'e basın.

Tüm listeyi görmek için 2'ye basın.

Bir kaydı silmek için listedeki ID numarasını kullanın.
