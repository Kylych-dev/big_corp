from ..product.models import ProductProxy
from django.conf import settings
from decimal import Decimal

class Cart():

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductProxy.objects.fitler(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item


    def serialize_cart(self):
        """
        Сериализует содержимое корзины в формат, подходящий для JSON
        """
        serialized_cart = []
        for product_id, quantity in self.cart.items():
            product = ProductProxy.objects.get(pk=product_id)
            serialized_cart.append({
                'product_id': product_id,
                'title': product.title,
                'quantity': quantity,
            })
        return serialized_cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'qty': quantity,
                'price': str(product.get_discount_price())
            }
        self.cart[product_id]['qty'] = quantity
        self.session.modified = True

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
            self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())



    # def __init__(self, request) -> None:
    #     self.session = request.session
    #     cart = self.session.get('session_key')
    #
    #     if not cart:
    #         cart = self.session['session_key'] = {}
    #
    #     self.cart = cart
    #

'''
add cart 
count cart

'''