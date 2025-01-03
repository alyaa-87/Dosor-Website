from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_recieved(sender, **kwargs):
	#add a 10 sec delay for paypal to send ipn and data
	time.sleep(10)

	# grab info that paypal send
	paypay_obj = sender
	# grab invoice
	my_Invoice = str(paypal_obj.invoice)

	#Match paypal invoice to order invoice
	#lookup the order
	my_Order = Order.objects.get(invoice=my_Invoice)

	#record payment
	my_Order.paid = True	
	my_Order.save()
	