from flask import Flask, render_template
import requests

app = Flask(__name__)

# Backend URL
BACKEND_URL = "http://flask-shop-app-service:80/shop/items"



@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL)
        items = response.json()
    except:
        items = []

    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
