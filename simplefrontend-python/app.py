from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Backend URL
BACKEND_URL = "http://flask-shop-backend:80/shop/items"



@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL)
        items = response.json()
    except:
        items = []

    return render_template('index.html', items=items)


@app.route('/reduce-stock', methods=['POST'])
def reduce_stock_frontend():
    item_id = int(request.form.get('item_id'))
    reduce_amount = int(request.form.get('reduce_amount'))

    # Prepare the data to send to the backend.
    data = {"id": item_id, "amount": reduce_amount}

    # Make a POST request to the backend.
    backend_response = requests.post("http://flask-shop-backend:80/shop/items/reduce", json=data)

    # Check the response from the backend and handle it as needed.
    if backend_response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Failed to reduce stock."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

