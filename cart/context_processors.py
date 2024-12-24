from .cart import Cart

# create context processor to make our cart work on all pages

def cart (request):
	return {'cart': Cart(request)}