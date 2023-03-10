

from store.models import Product
from decimal import Decimal


class Basket():
	'''
	A base Basket class, providing
	some default behaviors that can be inherited or
	overrided, as necessary.
	'''
	def __init__(self, request):
		self.session = request.session
		basket = self.session.get('skey')
		if 'skey' not in request.session:
			basket = self.session['skey'] = {}
		self.basket = basket


	def add(self, product, product_qty):
		'''
		Adding and updating the users basket session data
		'''
		product_id = str(product.id)
		
		if product_id in self.basket:
			self.basket[product_id]['qty']= product_qty
		else:
			self.basket[product_id] = {'price': str(product.price), 'qty':product_qty}

		self.save()

	def delete(self, product):
		'''
		delete users basket session data
		'''
		product_id = str(product)

		if product_id in self.basket:
			del self.basket[product_id]
			
		self.save()

	def update(self, product, qty):
		'''
		update users basket session data
		'''
		product_id = str(product)

		if product_id in self.basket:
			self.basket[product_id]['qty'] = qty
		self.save()


	def save(self):
		self.session.modified=True

	def __len__(self):
		'''
		get the basket data and count qty of items
		'''
		return sum(item['qty'] for item in self.basket.values())

	def __iter__(self):
		'''
		it allows us to do this class iterrable 
		'''

		product_ids = self.basket.keys()
		products = Product.objects.filter(id__in=product_ids)
		basket = self.basket.copy()
		for product in products:
			basket[str(product.id)]['product'] = product

		for item in basket.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['qty']
			yield item

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())