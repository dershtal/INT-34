from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return jsonify(status="200 OK")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)