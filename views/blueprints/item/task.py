from app import client
from models import db, Order, Delivery


def get_price(item_price, delivery_type):
    delivery = Delivery.query.filter(Delivery.delivery_type == delivery_type).first()
    price = item_price + delivery.price
    return price


@client.task()
def get_order(order_info):
    order = Order(customer_name=order_info["name"], customer_surname=order_info["surname"], phone=order_info["phone"],
                  item=order_info["item"],
                  order_city=order_info["city"], delivery_type=order_info["delivery_type"], payment_method=order_info["payment"],
                  comments=order_info["comments"], price=get_price(order_info["price"], order_info["delivery_type"]))
    db.session.add(order)
    db.session.commit()
