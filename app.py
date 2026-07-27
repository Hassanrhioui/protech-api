from flask import Flask, jsonify

app = Flask(__name__)

# Simulated Database (A list of dictionaries)
properties = [
    {"id": 1, "address": "123 DevOps Lane", "price": 500000, "status": "Available"},
    {"id": 2, "address": "456 Cloud Street", "price": 750000, "status": "Sold"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to PropTech Solutions API", "status": "Online"})

# New Route: Get all properties
@app.route('/api/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)