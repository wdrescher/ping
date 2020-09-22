from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth
import requests
from requests.auth import HTTPDigestAuth as httpDigest
import time as t


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
auth = HTTPDigestAuth()
pong_endpoint = 'https://drescherwe-pong.herokuapp.com/'

@auth.get_password
def get_pw(username):
    if username == 'vcu':
        return "rams"
    return None

@app.route("/", methods=['GET'])
@auth.login_required
def get():
        start = t.perf_counter()
        r = requests.get(pong_endpoint, auth=httpDigest('vcu', 'rams') )
        end = t.perf_counter()
        return jsonify({
                "total-time": end - start
        })

if __name__ == "__main__":
    app.run(debug=True)