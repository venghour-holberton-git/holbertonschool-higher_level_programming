from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
       return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as f:
         json_item = json.load(f)
    return render_template('items.html', items=json_item["items"] if "items" in json_item else [])

@app.route('/products')
def product_display():
    src = request.args.get('source')
    id = request.args.get('id')
    error_message = ""
    if src == "csv":
        data = read_csv("products.csv")
        categories = data[0]
        display_data = data[1:]
        if id is not None:
            display_data = list(filter(lambda item: filter_by_id(item, id), display_data))
            if display_data == []:
                error_message = "Product not found"
    elif src == "json":
        data = read_json("products.json")
        categories = [k for k, v in data[0].items()]
        display_data = [[v for k, v in d.items()] for d in data]
        if id is not None:
            display_data = list(filter(lambda item: filter_by_id(item, id), display_data))
            if display_data == []:
                error_message = "Product not found"
    elif src == "sql":
        data = get_database_data()
        categories = ['id', 'name', 'category', 'price']
        display_data = data
        if id is not None:
            display_data = list(filter(lambda item: filter_by_id(item, id), display_data))
            if display_data == []:
                error_message = "Product not found"
    else:
        error_message = "Wrong source"
        categories = []
        display_data = []
    return render_template("product_display.html", error_message = error_message, categories = categories, data = display_data)

@app.route('/populate')
def populate():
    create_database()
    return "data is populated"

@app.template_filter("check_items_len")
def check_items_len(items):
     return len(items) == 0

@app.template_filter("filter_id")
def filter_id(data, id):
    return filter(lambda item: item.id == id , data)

def read_csv(src):
    data = []
    with open(src, "r") as f:
          data = list(csv.reader(f))
    return data

def read_json(src):
    data = []
    with open(src, "r") as f:
        data = json.load(f)
    return data

def filter_by_id(item, id):
    return str(item[0]).strip() == id.strip()

def create_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

def get_database_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
               SELECT * FROM Products
           ''')
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)