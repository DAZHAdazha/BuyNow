# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session, g


from sqlalchemy import or_
import datetime
import json
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from .models import User, Cart, CartDetail, Order, OrderDetail, Product, Wishlist, WishlistDetail
from .decorator import login_required
from .utils import login_log
from app import app, db



# initialize a flask object by transmitting a "__name__"
# 1.convenient for flask frame to locate resource
# 2.convenient for locate errors when flask plug-in like Flask-SqlAlchemy goes wrong

# import config file
# ! app.config.from_object(config)
# very important! when dividing models file with this script!
# ! db.app = app
# to solve the problem of recursive reference
# ! db.init_app(app)

# solution for conflicts between jinja2 templates loading variable identifier
# "{{ }}" and jQuery-tmpl plug-in identifier"{{ }}",
# using for passing data from flask to json
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'

# setting session overdue time 
# from datetime import timedelta
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

app.secret_key = 'dazha'  # import os; app.secret_key = os.urandom(24) # 用os库自动生成24位的secret key

# if there is nested dictionary or object stored in dictionary,
# "object(dic).attr" could be used in HTML to visit variables
# or using the form of "object(dic)['attr']"
passing_data = {'signup_user': 0}


# this decorator will project to a url view function
@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index(): # view function
    try:
        if g.user:
            pop = 0
    except:
        pop = 1
    app.logger.info("Someone visited index.html")
    return render_template('./index.html', pop=pop)


# capture 404 error
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error("Error-404 happened.")
    return render_template('./error-404.html'), 404


# jump to HTML template if the requiring file exists
@app.route('/<file>')
def jump(file):
    try:
        return render_template('./' + file)
    except:
        app.logger.error("Error-404 happened.")
        return render_template('./error-404.html')


# similar to previous function
@app.route('/<file>')
def jump_to(file):
    try:
        app.logger.info("Someone visited " + file)
        return render_template('./' + file)
    except:
        app.logger.error("Error-404 happened.")
        return render_template('./error-404.html')


# to render page my-account and passing arguments of 3 type of task counts
@app.route('/my-account.html')
@login_required
def user():
    app.logger.info(g.user.username + " visited my-account.html")
    return render_template('./my-account.html')


#  handling GET and POST request
# for POST, register this user
# for GET, to render page register.html
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter(User.email == data['email']).first()
        # if the email had been used
        if user:
            app.logger.warning("This email(" + data['email'] + ")had been registered")
            return "This email had been registered"
        # else it could be signed up
        else:
            new_user = User(username=data['username'], password=data['password'],
                            email=data['email'], question=data['question'], answer=data['answer'])
            new_cart = Cart()
            new_wishlist = Wishlist()
            new_cart.user = new_user
            new_wishlist.user = new_user
            db.session.add(new_user)
            db.session.add(new_cart)
            db.session.add(new_wishlist)
            db.session.commit()
            session['user_email'] = data['email']
            app.logger.info("User " + data['username'] + " registered successfully!")
            return '1'
    elif request.method == 'GET':
        app.logger.info("Someone visited register.html")
        return render_template('./register.html')


# handling POST and GET request
# for POST, to log in the user
# for GET, to render log-in.html
@app.route('/login.html', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter(User.email == data['email']).first()
        # the user is existed
        if user:
            # the user's password is right
            if user.check_password(data['password']):
                session['user_email'] = user.email
                # user ticked the remember-me option
                if data['remember'] == 'true':
                    session.permanent = True
                else:
                    session.permanent = False
                app.logger.info("User " + user.username + " log-in successfully!")
                return '1'
            # the user's password is wrong
            else:
                app.logger.warning("This user(" + data['email'] + ")had entered wrong password.")
                return "Wrong password,try again"
        # the email is wrong
        else:
            app.logger.warning("This email(" + data['email'] + ")had not been registered.")
            return "Wrong email address,try again"
    else:
        app.logger.info("Someone visited login.html")
        return render_template('./login.html')


# A function used to handle request of forgetting password
@app.route('/forget.html', methods=['POST', 'GET'])
def forget():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter(User.email == data['email']).first()
        # the user is existed
        if user:
            # if question and answer are both correct
            if user.question == data['question'] and user.answer == data['answer']:
                user.password = data['password']
                db.session.add(user)
                db.session.commit()
                app.logger.warning(user.username + "had reset the password")
                return '1'
            # if question or answer goes wrong
            else:
                app.logger.warning("This account(" + data['email'] +
                                   ")cannot be reset because wrong answer to the question.")
                return "Wrong answer to the question."
        # if the email is wrong
        else:
            app.logger.warning("This email(" + data['email'] + ")had not been created yet.")
            return "Wrong email address,please try again"
    else:
        app.logger.info("Someone visited forget.html")
        return render_template('./forget.html')


# executing sequence： @before_request -> view function -> @context_processor
# context_processor: working as hook
@app.context_processor
def my_context_processor():
    # whether g object has user attribute
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        # note that hook functions warpped by this decorator need to return a dictionary(even it is empty)
        return {}


# logout view function, delete the sessions
@app.route('/logout/')
@login_required
def logout():
    del session['user_email']
    return redirect(url_for('login'))


# before_request: execute before requests,
# working as hook function and execute before view functions, and this function is
# a decorator, it could execute codes before view functions
@app.before_request
def my_before_quest():
    email = session.get('user_email')
    if email:
        user = User.query.filter(User.email == email).first()
        g.user = user


# A function used to handle entering cart.html
@app.route('/cart.html', methods=['POST', 'GET'])
@login_required
def cart():
    # post request is used to update the cart
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        current_time = datetime.datetime.now()
        total = data['total']
        product_sum = data['product_sum']
        order = Order(time=current_time, sum=total, product_number_sum=product_sum, user_id=g.user.id)
        user = User.query.filter(User.id==g.user.id).first()
        order.user = user
        db.session.add(order)
        for i in data['products']:
            order_detail = OrderDetail(product_id=i['id'],
                                       product_number=i['quantity'], product_sum=i['sum'], order_id=order.id)
            order_detail.order = order
            db.session.add(order_detail)
        for i in user.cart.cartDetails:
            db.session.delete(i)
        user.cart.sum = 0
        user.cart.product_number_sum = 0
        db.session.add(user.cart)
        db.session.commit()
        app.logger.info(g.user.username + " updated the cart")
        return "1"
    # get request is used to display all products in cart
    else:
        cart_id = g.user.cart_id
        cart = Cart.query.filter(Cart.id == cart_id).first()
        product_sum = cart.sum
        cart_info =[]
        for i in cart.cartDetails:
            new_info = {'product_id': i.product_id,
                        'product_detail': 'products-details' + str(i.product_id) + '.html',
                        'product_name': i.product.product_name,
                        'product_price': i.product.product_price,
                        'product_number': i.product_number,
                        'product_sum': i.product_sum,
                        'product_url': 'assets/img/cart/cart-' + str(i.product_id) + '.png'}
            cart_info.append(new_info)
        app.logger.info(g.user.username + " updated the cart")
        return render_template('./cart.html', product_sum=product_sum, cart_info=cart_info[::-1])


# A function used to handle updateCart request, only accepting POST method
@app.route('/updateCart', methods=['POST'])
@login_required
def updateCart():
    data = json.loads(request.form.get('data'))
    cart_id = g.user.cart_id
    cart = Cart.query.filter(Cart.id == cart_id).first()
    cart.sum = data["total"]
    cart.product_number_sum = len(data["products"])
    for i in cart.cartDetails:
        db.session.delete(i)
    for i in data["products"]:
        new_cartDetial = CartDetail(product_id=i["id"], product_number=i["quantity"],
                                    product_sum=i["sum"], cart_id=cart_id)
        db.session.add(new_cartDetial)
    db.session.add(cart)
    db.session.commit()
    app.logger.info(g.user.username + " updated the cart")
    return "1"


# A function used to handle addWishlist request, only accepting POST method
@app.route('/addWishlist', methods=['POST'])
@login_required
def addWishlist():
    wishlist_id = g.user.wishlist_id
    product_id = request.form.get("product_id")
    wishlist = Wishlist.query.filter(Wishlist.id == wishlist_id).first()
    flag = 0
    for i in wishlist.wishlistDetails:
        if i.product_id == int(product_id):
            flag = 1
            break
    if flag == 0:
        new_wishlistDetail = WishlistDetail(product_id=product_id, wishlist_id=wishlist_id)
        db.session.add(new_wishlistDetail)
        db.session.commit()
    app.logger.info(g.user.username + " added items to the wishlist")
    return render_template('./wishlist.html')


# A function used to handle removeWishlist request, only accepting POST method
@app.route('/removeWishlist', methods=['POST'])
@login_required
def removeWishlist():
    wishlist_id = g.user.wishlist_id
    product_id = request.form.get("product_id")
    wishlist = Wishlist.query.filter(Wishlist.id == wishlist_id).first()
    for i in wishlist.wishlistDetails:
        if i.product_id == int(product_id):
            db.session.delete(i)
    db.session.commit()
    app.logger.info(g.user.username + " removed items in the wishlist")
    return render_template('./wishlist.html')


# A function used to handle entering wishlist.html, accepting both GET and POST method
@app.route('/wishlist.html', methods=['POST', 'GET'])
@login_required
def wishlist():
    # for the GET method, display all items in wishlist
    if request.method == 'GET':
        wishlist_id = g.user.wishlist_id
        wishlist = Wishlist.query.filter(Wishlist.id == wishlist_id).first()
        wishlist_info = []
        for i in wishlist.wishlistDetails:
            new_info = {'product_id': i.product_id,
                        'product_detail': 'products-details' + str(i.product_id) + '.html',
                        'product_name': i.product.product_name,
                        'product_price': i.product.product_price,
                        'product_url': 'assets/img/cart/cart-' + str(i.product_id) + '.png'}
            wishlist_info.append(new_info)
        app.logger.info(g.user.username + " visited wishlist.html")
        return render_template('./wishlist.html', wishlist_info=wishlist_info[::-1])
    # for the POST method, update the item in wishlist to the cart
    else:
        user_id = g.user.id
        product_id = request.form.get('product_id')
        product_quantity = int(request.form.get('product_quantity'))
        user = User.query.filter(User.id == user_id).first()
        product = Product.query.filter(Product.id == product_id).first()
        flag = 0
        for i in user.cart.cartDetails:
            if int(i.product_id) != int(product_id):
                flag += 1
        if flag == len(user.cart.cartDetails):
            user.cart.product_number_sum += 1
            new_cartDetail = CartDetail(product_id=product_id, product_number=product_quantity,
                                        product_sum=product.product_price, cart_id=user.cart_id)
            db.session.add(new_cartDetail)
        else:
            for i in user.cart.cartDetails:
                if int(i.product_id) == int(product_id):
                    i.product_number += product_quantity
                    i.product_sum += product.product_price
                    db.session.add(i)
        user.cart.sum += product.product_price
        db.session.add(user.cart)
        db.session.commit()
        app.logger.info(g.user.username + " updated the cart")
        return '1'


# A function used to handle search request
@app.route('/search')
def search():
    q = request.args.get('q')
    products = Product.query.filter(or_(Product.product_name.contains(q), Product.product_price.contains(q))).all()
    search_info = []
    for i in products:
        new_info = {'product_id': i.id,
                    'product_name': i.product_name,
                    'product_price': i.product_price,
                    'product_url': 'assets/img/cart/cart-' + str(i.id) + '.png'}
        search_info.append(new_info)
    app.logger.info("Someone searched for the products")
    return render_template('./search.html', search_info=search_info)


# A function used to handle entering order.html
@app.route('/order.html')
@login_required
def order():
    user_id = g.user.id
    user = User.query.filter(User.id == user_id).first()
    order_info = []
    for i in user.orders:
        new_info = {'order_time': str(i.time)[:-7],
                    'order_sum': i.sum,
                    'order_product_number_sum': i.product_number_sum,
                    'order_id': i.id}
        order_info.append(new_info)
    app.logger.info(g.user.username + " checked the orders")
    return render_template('./order.html', order_info=order_info[::-1])


# A function used to handle orderDetails given order id. e.g. /orderDetail1, /orderDetail2
@app.route('/orderDetail<order_id>', methods=['GET'])
@login_required
def orderDetail(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    detail_info = []
    for i in order.orderDetails:
        new_info = {'product_name': i.product.product_name,
                    'product_number': i.product_number,
                    'product_sum': i.product_sum,
                    'product_href': 'products-details' + str(i.product_id) + '.html',
                    'product_url': 'assets/img/cart/cart-' + str(i.product_id) + '.png'
                    }
        detail_info.append(new_info)
    app.logger.info(g.user.username + " checked the order details")
    return render_template('./order-detail.html', order_id=order_id, detail_info=detail_info)

