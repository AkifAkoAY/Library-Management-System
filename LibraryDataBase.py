import sqlite3

DB_NAME = 'library.db'

def create_connection():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year_published INTEGER NOT NULL
            )
        ''')
        connection.commit()

def input_book_details():
    while True:
        try:
            title = input("Kitap Adi: ")
            if not title: raise ValueError("Kitap adi bos olamaz.")
            
            author = input("Yazar Adi: ")
            if not author: raise ValueError("Yazar adi bos olamaz.")
            
            year_published = int(input("Yayin Yili (sadece yil giriniz): "))
            return title, author, year_published
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Hata: Lutfen yil icin gecerli bir sayi girin.")
            else:
                print(f"Hata: {e}")

def add_book(title, author, year_published):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, year_published)
            VALUES (?, ?, ?)
        ''', (title, author, year_published))
        connection.commit()
    return "Kitap basariyla eklendi."

def get_all_books():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return books

def delete_book(book_id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        if not cursor.fetchone():
            return "Hata: Bu ID'ye sahip kitap bulunamadi."
            
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        connection.commit()
    return "Kitap basariyla silindi."

def update_book(book_id, title, author, year_published):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE books 
            SET title = ?, author = ?, year_published = ? 
            WHERE id = ?
        ''', (title, author, year_published, book_id))
        
        if cursor.rowcount == 0:
            return "Hata: Guncellenecek kitap bulunamadi."
            
        connection.commit()
    return "Kitap basariyla guncellendi."

def main():
    create_connection()
    print("--- Kutuphane Yonetim Sistemi Baslatildi ---")
    
    while True:
        print("\n=== MENU ===")
        print("1. Kitap Ekle")
        print("2. Kitaplari Listele")
        print("3. Kitap Sil")
        print("4. Kitap Guncelle")
        print("5. Cikis")
        
        choice = input("Seciminiz (1-5): ")
        
        if choice == '1':
            title, author, year_published = input_book_details()
            message = add_book(title, author, year_published)
            print(message)
            
        elif choice == '2':
            books = get_all_books()
            if books:
                print("\n--- Kitap Listesi ---")
                print(f"{'ID':<5} {'Baslik':<30} {'Yazar':<20} {'Yil'}")
                print("-" * 65)
                for book in books:
                    print(f"{book[0]:<5} {book[1]:<30} {book[2]:<20} {book[3]}")
            else:
                print("\nKutuphanede hic kitap yok.")
                
        elif choice == '3':
            try:
                book_id = int(input("Silinecek Kitap ID'sini girin: "))
                message = delete_book(book_id)
                print(message)
            except ValueError:
                print("Hata: Gecerli bir ID numarasi girin.")
                
        elif choice == '4':
            try:
                book_id = int(input("Guncellenecek Kitap ID'sini girin: "))
                print("--- Yeni Bilgileri Girin ---")
                new_title, new_author, new_year_published = input_book_details()
                message = update_book(book_id, new_title, new_author, new_year_published)
                print(message)
            except ValueError:
                print("Hata: Gecerli bir ID numarasi girin.")
                
        elif choice == '5':
            print("Programdan cikiliyor. Iyi gunler!")
            break 
            
        else:
            print("Gecersiz secim, lutfen tekrar deneyin.")

if __name__ == "__main__":
    main()