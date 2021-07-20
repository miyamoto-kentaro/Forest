import os
from flask import request, render_template
from flask_bootstrap import Bootstrap

from models import db, Product
from app import app
from collect import collect_product
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/product_list')
# def product_list():
#     # # メンバー一覧表示
#     products = Product.query.all()
#     for product in products:
#         print(product)
#     return render_template('product_list.html', products=products)


@app.route("/product_list", methods=["POST"])
def product_list():
    product_name = str(request.form["product_name"])
    print('search_key:', product_name)
    products = Product.query.filter(Product.search_key == product_name).all()
    # collect_product(product_name)
    # print(len(products))
    if len(products) == 0:
        collect_product(product_name)
        print('no products')
        products = Product.query.filter(
            Product.search_key == product_name).all()
    # print(products)
    return render_template('product_list.html', products=products)


@app.route('/test')
def test_bootstrap():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=os.environ["PORT"])
