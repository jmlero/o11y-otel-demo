from flask import Flask, jsonify, request
import random
import time
import sys
import logging


app = Flask(__name__)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# This is a simulated in-memory database for our shop items.
shop_items = [
    {"id": 1, "name": "apple", "price": 0.5, "stock": 100},
    {"id": 2, "name": "banana", "price": 0.2, "stock": 50},
]

@app.route('/shop/items', methods=['GET'])
def get_items():
    return jsonify(shop_items), 200

@app.route('/shop/items', methods=['POST'])
def add_item():
    data = request.json
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({"message": "Invalid data."}), 400

    new_item = {
        "id": len(shop_items) + 1,
        "name": data['name'],
        "price": float(data['price']),
        "stock": int(data['stock'])
    }
    shop_items.append(new_item)
    return jsonify(new_item), 201

@app.route('/shop/items/reduce', methods=['POST'])
def reduce_stock():
    data = request.json
    if not data or 'id' not in data or 'amount' not in data:
        return jsonify({"message": "Invalid data."}), 400

    item_id = data['id']
    amount = data['amount']

    item = next((item for item in shop_items if item['id'] == item_id), None)
    if not item:
        return jsonify({"message": "Item not found."}), 404

    if item['stock'] - amount < 0:
        return jsonify({"message": "Stock can't be negative."}), 400

    # Generate a random sleep time 
    sleep_time = random.uniform(0, 2)
    time.sleep(sleep_time)  # Introduce the random sleep

     # Log the request and sleep duration to stdout
    logger.info(f"Request to reduce stock for item ID {item_id}: {amount}")

    item['stock'] -= amount
    return jsonify(item), 200

if __name__ == '__main__':
    app.run(debug=True)
    
