from store.models import Product, Profile

class Cart():
	def __init__(self, request):
		self.session = request.session
		#get request
		self.request = request
		# Get current key if exist
		cart = self.session.get('session_key')

		#if user is new, create new key
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		# Make cart available on all pages
		self.cart = cart

	def db_add(self, product, quantity):
		product_id = str(product)
		product_qty = str(quantity)

		#logic
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		#deal with logged in user
		if self.request.user.is_authenticated:
			#get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# change single quotation in dictionary to double in order to user json (javascript)
			carty = str(self.cart)
			carty = carty.replace("\'","\"")
			# save carty to profile model
			current_user.update(old_cart=str(carty))


	def add(self, product, quantity):
		product_id = str(product.id)
		product_qty = str(quantity)

		#logic
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		#deal with logged in user
		if self.request.user.is_authenticated:
			#get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# change single quotation in dictionary to double in order to user json (javascript)
			carty = str(self.cart)
			carty = carty.replace("\'","\"")
			# save carty to profile model
			current_user.update(old_cart=str(carty))


	def cart_total(self):
		#get prodcut ids
		product_ids = self.cart.keys()
		#lookup keys in our product db model
		products = Product.objects.filter(id__in=product_ids)
		#get quantity
		quantities = self.cart
		# start counting at zero
		total = 0
		for key, value in quantities.items():
			#convert key string to in so we can calculate
			key = int(key)
			for product in products:
				if product.id == key:
					if product.is_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)

		
		return total	

	def __len__(self):
		return len(self.cart)

	def get_prods(self):
		#get ids from cart		
		product_ids = self.cart.keys()
		#use ids to lookup products and database model
		products = Product.objects.filter(id__in=product_ids)


		return products


	def get_quants(self):
		quantities = self.cart
		return quantities

	def update(self, product, quantity):
		product_id = str(product)
		product_qty =  int(quantity)


		# Get cart
		ourcart = self.cart
		#update dicitonary/cart
		ourcart[product_id] = product_qty

		self.session.modified = True

		#deal with logged in user
		if self.request.user.is_authenticated:
			#get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# change single quotation in dictionary to double in order to user json (javascript)
			carty = str(self.cart)
			carty = carty.replace("\'","\"")
			# save carty to profile model
			current_user.update(old_cart=str(carty))
			
		thing = self.cart
		return thing


	def delete(self, product):
		product_id = str(product)
		#del from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True

		#deal with logged in user
		if self.request.user.is_authenticated:
			#get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# change single quotation in dictionary to double in order to user json (javascript)
			carty = str(self.cart)
			carty = carty.replace("\'","\"")
			# save carty to profile model
			current_user.update(old_cart=str(carty))