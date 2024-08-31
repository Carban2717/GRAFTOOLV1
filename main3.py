import os
import random
import time
from colorama import Fore, init
from flask import Flask, request

init(autoreset=True)

app = Flask(__name__)

@app.route('/')
def index():
    # İstemcinin IP adresini almak için X-Forwarded-For başlığını kontrol et
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"Your IP address is {ip}"

def start_ip_logger():
    app.run(host='0.0.0.0', port=8080)

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
    print(Fore.GREEN + "[04] IP Logger")  # Yeni seçenek

def generate_random_gmails(count):
    gmails = []
    for _ in range(count):
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
        gmails.append(f'{username}@gmail.com')
    return gmails

def generate_random_carts(count):
    carts = []
    for _ in range(count):
        number = ''.join(random.choices('0123456789', k=16))
        exp_month = str(random.randint(1, 12)).zfill(2)
        exp_year = str(random.randint(24, 34))  # Gelecek yıllar
        cvv = ''.join(random.choices('0123456789', k=3))
        carts.append(f'{number} | {exp_month}/{exp_year} | {cvv}')
    return carts

def main():
    while True:
        print_menu()
        choice = input(Fore.GREEN + "Seçiminizi yapın (1, 2, 3 veya 4): ")

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
            print(Fore.GREEN + "IP Logger başlatılıyor...")
            start_ip_logger()
        else:
            clear_screen()
            print(Fore.RED + "Geçersiz seçim. Lütfen tekrar deneyin.")
            time.sleep(1)

if __name__ == "__main__":
    main()
