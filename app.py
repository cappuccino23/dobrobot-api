from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    request_data = request.get_json()
    return jsonify(request_data)


if __name__ == '__main__':
    app.run()
