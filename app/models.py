from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# A table defined to model Users
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    question = db.Column(db.String(40), nullable=False)
    answer = db.Column(db.String(40), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))

    def __init__(self, *args, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        question = kwargs.get('question')
        answer = kwargs.get('answer')
        email = kwargs.get('email')
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.question = question
        self.answer = answer

    # Function used to convert raw password to hashed version
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    def __repr__(self):
        return '<id:%d username:%s email:%s password:%s question:%s answer:%s>' % (self.id, self.username, self.email,
                                                            self.password, self.question, self.answer)


# A table defined to model Orders
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    sum = db.Column(db.Float, nullable=True)
    product_number_sum = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref=db.backref("orders"))


# A table defined to model Cart
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sum = db.Column(db.Float, default=0)
    product_number_sum = db.Column(db.Integer, default=0)
    user = db.relationship('User', uselist=False, backref=db.backref("cart"))


# A table defined to model Wishlist
class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_number_sum = db.Column(db.Integer, default=0)
    user = db.relationship('User', uselist=False, backref=db.backref("wishlist"))


# A table defined to model Cart Details
class CartDetail(db.Model):
    __tablename__ = 'cartDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    product_number = db.Column(db.Integer, nullable=True)
    product_sum = db.Column(db.Float, nullable=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=True)
    cart = db.relationship('Cart', backref=db.backref("cartDetails"))
    product = db.relationship('Product')


# A table defined to model Wishlist Details
class WishlistDetail(db.Model):
    __tablename__ = 'wishlistDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=True)
    wishlist = db.relationship('Wishlist', backref=db.backref("wishlistDetails"))
    product = db.relationship('Product')


# A table defined to model Order Details
class OrderDetail(db.Model):
    __tablename__ = 'orderDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    product_number = db.Column(db.Integer, nullable=True)
    product_sum = db.Column(db.Float, nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    order = db.relationship('Order', backref=db.backref("orderDetails"))
    product = db.relationship('Product')


# A table defined to model Products
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.Text(50), nullable=True)
    product_price = db.Column(db.Float(50), nullable=True)

