from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def get_ec2_public_ip():
    return os.getenv('EC2_PUBLIC_DNS')

if __name__ == '__main__':
    ec2_ip = get_ec2_public_ip()
    
    if ec2_ip:
        app.run(host='0.0.0.0', port=5000)  
    else:
        raise Exception("EC2 IP was not found in environment variables")
