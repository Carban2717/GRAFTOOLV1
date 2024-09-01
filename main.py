import os
import random
import time
import requests
import re
from faker import Faker
from colorama import Fore, init

init(autoreset=True)

# Desteklenen ülkeler ve kodları
countries = {
    'USA': 'en_US',
    'Germany': 'de_DE',
    'France': 'fr_FR',
    'Italy': 'it_IT',
    'Spain': 'es_ES',
    'UK': 'en_GB',
    'Canada': 'en_CA',
    'Australia': 'en_AU',
    'Japan': 'ja_JP',
    'China': 'zh_CN',
    'Brazil': 'pt_BR',
    'India': 'en_IN',
    'Russia': 'ru_RU',
    'South Africa': 'en_ZA',
    'Mexico': 'es_MX',
    'Argentina': 'es_AR',
    'Chile': 'es_CL',
    'Colombia': 'es_CO',
    'Peru': 'es_PE',
    'Venezuela': 'es_VE',
    'Saudi Arabia': 'ar_SA',
    'United Arab Emirates': 'en_AE',
    'Turkey': 'tr_TR',
    'Egypt': 'ar_EG',
    'Israel': 'en_IL',
    'Pakistan': 'en_PK',
    'Thailand': 'th_TH',
    'South Korea': 'ko_KR',
    'Malaysia': 'ms_MY',
    'Singapore': 'en_SG',
    'Philippines': 'en_PH',
    'Vietnam': 'vi_VN',
    'New Zealand': 'en_NZ',
    'Ireland': 'en_IE',
    'Sweden': 'sv_SE',
    'Norway': 'no_NO',
    'Denmark': 'da_DK',
    'Finland': 'fi_FI',
    'Greece': 'el_GR',
    'Portugal': 'pt_PT',
    'Poland': 'pl_PL',
    'Czech Republic': 'cs_CZ',
    'Hungary': 'hu_HU',
    'Romania': 'ro_RO',
    'Bulgaria': 'bg_BG',
    'Ukraine': 'uk_UA',
    'Belarus': 'be_BY',
    'Lithuania': 'lt_LT',
    'Latvia': 'lv_LV',
    'Estonia': 'et_EE',
    'Slovakia': 'sk_SK',
    'Croatia': 'hr_HR'
}

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
    print(Fore.GREEN + "[07] Rastgele Telefon Numarası")  # Yeni seçenek

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

def generate_phone_numbers(locale, count=20):
    fake = Faker(locale)
    return [fake.phone_number() for _ in range(count)]

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
        choice = input(Fore.GREEN + "Seçiminizi yapın (1, 2, 3, 4, 5, 6 veya 7): ")

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
            user_activity_log.append(f"Şifre testi yapıldı: {password} - Sonuç: {result}")
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '7':
            clear_screen()
            print(Fore.WHITE + "Ülke kodu (örn. tr_TR):")
            locale = input()
            print(Fore.WHITE + "Kaç telefon numarası üretmek istersiniz?")
            count = int(input())
            phone_numbers = generate_phone_numbers(locale, count)
            for number in phone_numbers:
                print(number)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        else:
            clear_screen()
            print(Fore.RED + "Geçersiz seçim. Lütfen geçerli bir seçenek girin.")

if __name__ == "__main__":
    main()
