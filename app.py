
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    with open('/data/data/com.termux/files/home/ip_address.txt', 'w') as f:
        f.write(user_ip)
    return f"Your IP address is {user_ip}"

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
