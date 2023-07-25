from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hola', methods=['GET'])
def hola():
    data = {"key": "value"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
