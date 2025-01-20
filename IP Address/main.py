from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/network/ip=<ip>', methods=['GET'])
def get_ip_info(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)