import os
import random
import time
import re
import requests
from colorama import Fore, init

init(autoreset=True)

# Kullanıcı işlemlerini takip etmek için bir liste
user_activity_log = []

def clear_screen():
    os.system('clear')

def print_menu():
    clear_screen()
    print(Fore.BLUE + """
   ____ ____      _    _____ _____ ___   ___  _     
  / ___|  _ \    / \  |  ___|_   _/ _ \ / _ \| |    
 | |  _| |_) |  / _ \ | |_    | || | | | | | | |    
 | |_| |  _ <  / ___ \|  _|   | || |_| | |_| | |___ 
  \____|_| \_\/_/   \_\_|     |_| \___/ \___/|_____|
                                                    
""")
    print(Fore.RED + "Developer: carbans2717")
    print(Fore.GREEN + "[01] Çıkış")
    print(Fore.GREEN + "[02] Random Gmail")
    print(Fore.GREEN + "[03] Random Cart Generator")
    print(Fore.GREEN + "[04] IP Adresi Sorgulama")
    print(Fore.GREEN + "[05] Admin Panel")
    print(Fore.GREEN + "[06] Şifre Gücü Testi")
    print(Fore.GREEN + "[07] E-posta Doğrulama")
    print(Fore.GREEN + "[08] Geçici E-posta ve Gelen E-postalar")  # Yeni seçenek

def generate_random_gmails(count):
    gmails = []
    for _ in range(count):
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
        gmails.append(f'{username}@gmail.com')
    user_activity_log.append(f"Generated {count} random Gmail addresses.")
    return gmails

def generate_random_carts(count):
    carts = []
    for _ in range(count):
        number = ''.join(random.choices('0123456789', k=16))
        exp_month = str(random.randint(1, 12)).zfill(2)
        exp_year = str(random.randint(24, 34))  # Gelecek yıllar
        cvv = ''.join(random.choices('0123456789', k=3))
        carts.append(f'{number} | {exp_month}/{exp_year} | {cvv}')
    user_activity_log.append(f"Generated {count} random credit card details.")
    return carts

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        if data['status'] == 'fail':
            print(Fore.RED + "Hatalı IP adresi girdiniz.")
            return

        print(Fore.GREEN + f"IP Adresi: {data['query']}")
        print(Fore.GREEN + f"Ülke: {data['country']}")
        print(Fore.GREEN + f"Bölge: {data['regionName']}")
        print(Fore.GREEN + f"Şehir: {data['city']}")
        print(Fore.GREEN + f"ISP: {data['isp']}")
        print(Fore.GREEN + f"Organizasyon: {data['org']}")
        print(Fore.GREEN + f"AS: {data['as']}")
        print(Fore.GREEN + f"Posta Kodu: {data['zip']}")
        print(Fore.GREEN + f"Enlem: {data['lat']}")
        print(Fore.GREEN + f"Boylam: {data['lon']}")
        
        # Kullanıcı işlemi kaydediliyor
        user_activity_log.append(f"IP sorgulandı: {ip_address} - {data['country']}, {data['city']}, {data['isp']}")
    except requests.RequestException as e:
        print(Fore.RED + "Bir hata oluştu:", e)

def check_password_strength(password):
    if len(password) < 8:
        return "Şifre çok kısa. En az 8 karakter olmalı."

    # Şifre karmaşıklığını kontrol et
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    digit = re.compile(r'\d')
    special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    
    if not lower.search(password):
        return "Şifre en az bir küçük harf içermeli."
    if not upper.search(password):
        return "Şifre en az bir büyük harf içermeli."
    if not digit.search(password):
        return "Şifre en az bir rakam içermeli."
    if not special.search(password):
        return "Şifre en az bir özel karakter içermeli."
    
    return "Şifre güçlü."

def check_email(email):
    """E-posta adresinin geçerli olup olmadığını kontrol eder."""
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not re.match(email_regex, email):
        return "Geçersiz e-posta formatı."
    
    return "E-posta adresi geçerli."

def get_temp_email():
    """Temp-mail sitesinden geçici bir e-posta adresi alır."""
    try:
        response = requests.get("https://temp-mail.org/en/")
        # Bu URL üzerinden doğrudan geçici e-posta almak mümkün olmayabilir. 
        # Gerçek bir temp-mail API entegrasyonu gereklidir.
        # Burada örnek olarak sabit bir e-posta adresi döneceğiz.
        return "example@temp-mail.org"  # Burayı gerçek temp-mail API çağrısıyla değiştirin
    except requests.RequestException as e:
        print(Fore.RED + "Bir hata oluştu:", e)
        return None

def get_emails(temp_email):
    """Geçici e-posta adresine gelen e-postaları kontrol eder."""
    try:
        # Bu URL üzerinden doğrudan e-postaları almak mümkün olmayabilir. 
        # Gerçek bir temp-mail API entegrasyonu gereklidir.
        # Burada örnek olarak sabit bir e-posta mesajı döneceğiz.
        print(Fore.GREEN + f"{temp_email} adresine gelen e-postalar:")
        # Örnek e-posta verileri
        emails = [
            "From: example1@example.com\nSubject: Test Email 1\n\nThis is a test email.",
            "From: example2@example.com\nSubject: Test Email 2\n\nThis is another test email."
        ]
        for email in emails:
            print(Fore.GREEN + email)
    except requests.RequestException as e:
        print(Fore.RED + "Bir hata oluştu:", e)

def admin_panel():
    clear_screen()
    print(Fore.RED + "Admin Password:")
    password = input()
    if password == "graftooladminkey":
        clear_screen()
        print(Fore.GREEN + "Admin terminaline hoş geldiniz!")
        print(Fore.GREEN + "Kullanıcı aktiviteleri:")
        for activity in user_activity_log:
            print(Fore.GREEN + activity)
        input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
    else:
        print(Fore.RED + "Yanlış şifre. Geri dönülüyor...")
        time.sleep(1)

def main():
    while True:
        print_menu()
        choice = input(Fore.GREEN + "Seçiminizi yapın (1, 2, 3, 4, 5, 6, 7 veya 8): ")

        if choice == '1':
            clear_screen()
            print(Fore.GREEN + "Çıkış yapılıyor...")
            time.sleep(1)
            break
        elif choice == '2':
            clear_screen()
            print(Fore.GREEN + "50 adet Random Gmail adresi:")
            gmails = generate_random_gmails(50)
            for gmail in gmails:
                print(gmail)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '3':
            clear_screen()
            print(Fore.GREEN + "50 adet Rastgele Kredi Kartı bilgisi:")
            carts = generate_random_carts(50)
            for cart in carts:
                print(cart)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '4':
            clear_screen()
            print(Fore.WHITE + "IP Adresi:")
            ip_address = input()
            clear_screen()
            print(Fore.GREEN + f"{ip_address} adresi sorgulanıyor...")
            get_ip_info(ip_address)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '5':
            admin_panel()
        elif choice == '6':
            clear_screen()
            print(Fore.WHITE + "Şifreyi girin:")
            password = input()
            result = check_password_strength(password)
            print(Fore.GREEN + result)
            user_activity_log.append(f"Şifre testi yapıldı: {password} - Sonuç: {result}")  # Şifreyi admin paneline kaydet
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '7':
            clear_screen()
            print(Fore.WHITE + "Doğrulamak istediğiniz e-posta adresini girin:")
            email = input()
            result = check_email(email)
            print(Fore.GREEN + result)
            user_activity_log.append(f"E-posta testi yapıldı: {email} - Sonuç: {result}")  # E-posta testi admin paneline kaydedildi
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '8':
            clear_screen()
            print(Fore.WHITE + "Geçici e-posta almak için 'al' yazın:")
            action = input()
            if action.lower() == 'al':
                temp_email = get_temp_email()
                if temp_email:
                    print(Fore.GREEN + f"Geçici E-posta Adresi: {temp_email}")
                    print(Fore.WHITE + "E-posta adresinize gelen e-postalar:")
                    get_emails(temp_email)
                else:
                    print(Fore.RED + "Geçici e-posta alınamadı.")
            else:
                print(Fore.RED + "Geçici e-posta alınmadı.")
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        else:
            clear_screen()
            print(Fore.RED + "Geçersiz seçim. Lütfen tekrar deneyin.")
            time.sleep(1)

if __name__ == "__main__":
    main()
