from exts import db
from werkzeug.security import generate_password_hash, check_password_hash

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
    # cart_number = db.Column(db.Integer, default=0)
    # wishlist_number = db.Column(db.Integer, default=0)

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
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
    def __repr__(self):
        return '<id:%d username:%s email:%s password:%s question:%s answer:%s>' % (self.id, self.username, self.email,
                                                            self.password, self.question, self.answer)


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    sum = db.Column(db.Float, nullable=True)
    product_number_sum = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # 第一参数为要关联的表的模型的名字,作为正向引用，backref表示反向引用，以后可以通过User.orders反向引用来通过user对象查找
    # 对应order表的数据
    user = db.relationship('User', backref=db.backref("orders"))


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sum = db.Column(db.Float, default=0)
    product_number_sum = db.Column(db.Integer, default=0)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # 第一参数为要关联的表的模型的名字,作为正向引用，backref表示反向引用，以后可以通过User.orders反向引用来通过user对象查找
    # 对应order表的数据
    user = db.relationship('User', uselist=False, backref=db.backref("cart"))


class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_number_sum = db.Column(db.Integer, default=0)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # 第一参数为要关联的表的模型的名字,作为正向引用，backref表示反向引用，以后可以通过User.orders反向引用来通过user对象查找
    # 对应order表的数据
    user = db.relationship('User', uselist=False, backref=db.backref("wishlist"))


class CartDetail(db.Model):
    __tablename__ = 'cartDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    product_number = db.Column(db.Integer, nullable=True)
    product_sum = db.Column(db.Float, nullable=True)

    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=True)
    cart = db.relationship('Cart', backref=db.backref("cartDetails"))
    product = db.relationship('Product')


class WishlistDetail(db.Model):
    __tablename__ = 'wishlistDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)

    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=True)
    wishlist = db.relationship('Wishlist', backref=db.backref("wishlistDetails"))
    product = db.relationship('Product')


class OrderDetail(db.Model):
    __tablename__ = 'orderDetail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    product_number = db.Column(db.Integer, nullable=True)
    product_sum = db.Column(db.Float, nullable=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    order = db.relationship('Order', backref=db.backref("orderDetails"))
    product = db.relationship('Product')
    # foreign key
    # order id


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.Text(50), nullable=True)
    product_price = db.Column(db.Float(50), nullable=True)

