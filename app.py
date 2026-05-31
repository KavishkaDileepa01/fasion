from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Sample product data
products = [
    {
        "id": 1,
        "name": "Classic Denim Jacket",
        "price": 89.99,
        "category": "Jackets",
        "image": "https://readdy.ai/api/search-image?query=stylish%20modern%20denim%20jacket",
        "description": "Premium quality, perfect for any season",
        "sizes": ["S", "M", "L", "XL"],
        "colors": ["Blue", "Black"],
        "material": "Denim"
    },
    {
        "id": 2,
        "name": "Essential White Tee",
        "price": 29.99,
        "category": "T-shirts",
        "image": "https://readdy.ai/api/search-image?query=premium%20white%20t-shirt",
        "description": "100% organic cotton, ultra-soft",
        "sizes": ["XS", "S", "M", "L", "XL"],
        "colors": ["White"],
        "material": "Cotton"
    },
    # Add more products as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/products/filter', methods=['POST'])
def filter_products():
    filters = request.json
    filtered_products = products
    
    if filters.get('category'):
        filtered_products = [p for p in filtered_products if p['category'] == filters['category']]
    
    if filters.get('min_price'):
        filtered_products = [p for p in filtered_products if p['price'] >= float(filters['min_price'])]
    
    if filters.get('max_price'):
        filtered_products = [p for p in filtered_products if p['price'] <= float(filters['max_price'])]
    
    if filters.get('sizes'):
        filtered_products = [p for p in filtered_products if any(size in p['sizes'] for size in filters['sizes'])]
    
    if filters.get('colors'):
        filtered_products = [p for p in filtered_products if any(color in p['colors'] for color in filters['colors'])]
    
    if filters.get('materials'):
        filtered_products = [p for p in filtered_products if p['material'] in filters['materials']]
    
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True) 