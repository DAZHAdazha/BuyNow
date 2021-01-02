from app import app
import logging
from app.models import User, Cart, CartDetail, Order, OrderDetail, Product, Wishlist, WishlistDetail
# if __name__ == '__main__':
    # db.drop_all()

    # db.create_all()

handler = logging.FileHandler('all.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
app.logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

info_handler = logging.FileHandler('info.log')
info_filter = logging.Filter()
info_filter.filter = lambda record: record.levelno < logging.WARNING
info_handler.setFormatter(formatter)
info_handler.addFilter(info_filter)
app.logger.addHandler(info_handler)

warning_handler = logging.FileHandler('warning.log')
warning_filter = logging.Filter()
warning_filter.filter = lambda record:  record.levelno == logging.WARNING
warning_handler.setFormatter(formatter)
warning_handler.addFilter(warning_filter)
app.logger.addHandler(warning_handler)

error_handler = logging.FileHandler('error.log')
error_filter = logging.Filter()
error_filter.filter = lambda record: record.levelno == logging.ERROR
error_handler.setFormatter(formatter)
error_handler.addFilter(error_filter)
app.logger.addHandler(error_handler)

    # app.logger.info("!!!")
    # app.logger.warning("Warning msg")
    # app.logger.error("Error msg!!!")

    # user1 = User(username="dazha", email="758343984@qq.com", password="fengyunjia", question="e", answer="w")
    # cart1 = Cart(user_id=user1.id)
    # cart1.user = user1
    # product1 = Product(product_name="Bluetooth Headphone", product_price=250)
    # product2 = Product(product_name="Protable Speakers", product_price=200)
    # product3 = Product(product_name="Digital Camera", product_price=200)
    # product4 = Product(product_name="Smart Watch", product_price=150)
    # product5 = Product(product_name="New Smart Phone", product_price=175)
    # db.session.add(user1)
    # db.session.add(cart1)
    # db.session.add(product1)
    # db.session.add(product2)
    # db.session.add(product3)
    # db.session.add(product4)
    # db.session.add(product5)
    # db.session.commit()

    # current_time = datetime.datetime.now()
    # order1 = Order(time=current_time, sum=3989899800, product_number_sum=3, user_id=1)
    # order2 = Order(time=current_time, sum=500, product_number_sum=5, user_id=1)
    # first_user = User.query.filter(User.id == 1).first()
    # order1.user= first_user
    # order2.user= first_user
    #
    # first_order = Order.query.filter(Order.id == 1).first()
    # print(first_order.sum)
    # print(first_order.user_id)
    # print(first_order.user.username)
    # db.session.add(order1)
    # db.session.add(order2)
    #
    # orderDetail1 = OrderDetail(product_id=1, product_number=3, product_sum=30099, order_id=1)
    # orderDetail2 = OrderDetail(product_id=2, product_number=4, product_sum=700, order_id=1)
    # db.session.add(orderDetail1)
    # db.session.add(orderDetail2)
    #
    # db.session.commit()
    # print(first_user.orders[0].orderDetails[0].product_id)
    # first_product = Product.query.filter(Product.id == 1).first()
    # print(first_user.orders[0].orderDetails[0].product.product_name)
    # print(first_user.orders[4].orderDetails[4].product.product_name)
    # print(first_user.cart.id)
    # print(first_user.cart.sum)
    # print(first_user.cart.product_number_sum)
    # first_cart = Cart.query.filter(Cart.id == 1).first()
    # print(first_cart)
    # print(first_cart.user.username)
    # cartDetail1 = CartDetail(product_id=1, product_number=3, product_sum=750, cart_id=first_user.cart_id)
    # now_user = first_user
    # now_user.cart.sum=cartDetail1.product_sum
    # now_user.cart.product_number_sum = cartDetail1.product_number
    # cartDetail1.cart = now_user.cart
    # db.session.add(cartDetail1)
    # db.session.add(now_user.cart)
    # db.session.commit()
    # print(first_user.cart.cartDetails[0].product_number)
    # print(first_user.cart.cartDetails[1].product_number)
app.run(debug="True")