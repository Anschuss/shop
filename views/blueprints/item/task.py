from app import client
from login_and_model import db, Order, Delivery


def get_price(item_price, delivery_type):
    delivery = Delivery.query.filter(Delivery.delivery_type == delivery_type).first()
    price = item_price + delivery.price
    return price


@client.task(bind=True)
def get_order(self, order_info):
    order = Order(phone=order_info["phone"], user_id=order_info["id"], item=order_info["item"],
                  order_city=order_info["city"], delivery_type=order_info["delivery_type"],
                  payment_method=order_info["payment"],
                  comments=order_info["comments"], price=get_price(order_info["price"], order_info["delivery_type"]))
    db.session.add(order)
    db.session.commit()


@client.task(bind=True)
def get_status(self, order_data):
    order = Order.query.filter(Order.id == order_data["id"]).first()
    if order_data["status"] == "Nicht Schaffen":
        order.status = False
    else:
        order.status = True

    db.session.commit()
