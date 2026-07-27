from flask import Flask, jsonify, render_template # Add render_template

app = Flask(__name__)

properties = [
    {
        "id": 1,
        "address": "123 Oasis Lane",
        "price": 500000,
        "status": "Available",
        "type": "Luxury Villa",
        "bedrooms": 4,
        "bathrooms": 3,
        "image": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 2,
        "address": "456 Atlas Street",
        "price": 750000,
        "status": "Sold",
        "type": "Modern Loft",
        "bedrooms": 3,
        "bathrooms": 2,
        "image": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=900&q=80"
    },
    {
        "id": 3,
        "address": "789 Skyline Avenue",
        "price": 980000,
        "status": "Available",
        "type": "Penthouse",
        "bedrooms": 5,
        "bathrooms": 4,
        "image": "https://images.unsplash.com/photo-1460317442991-0ec209397118?auto=format&fit=crop&w=900&q=80"
    }
]

@app.route('/')
def home():
    # This tells Flask to look in the /templates folder for index.html
    return render_template('index.html')

@app.route('/api/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)