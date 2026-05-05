from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Item, Cart, CartItem, Transaction
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

PRICE_IDS = ['price_1TSmKY1173BLi1iPSoZutfH7']

def store(request):

    if request.user.is_authenticated:
        items = Item.objects.all()
        return render(request, 'store/store.html', {'items': items})
    return render(request, 'home.html')




@login_required
def add_to_cart(request, item_id):
    
    product = get_object_or_404(Item, id=item_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')

@login_required
def cart(request):
    print(settings.STRIPE_SECRET_KEY)
    price_objs = [stripe.Price.retrieve(pid) for pid in PRICE_IDS]
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart, 'prices' : price_objs})

@login_required
def checkout(request):


    price_id = request.POST.get('price_id')
    transaction = Transaction.objects.create(
        user = request.user,
        stripe_session_id = '',
        amount = 0, 
        paid = False
    )
    checkout_session = stripe.checkout.Session.create(
        line_items= [
            {
                'price': price_id,
                'quantity': 1 # change later
            }
        ],
        mode = 'payment',
        success_url = request.build_absolute_uri(reverse('store') + '?success=1&session_id={CHECKOUT_SESSION_ID}'),
        cancel_url = request.build_absolute_uri(reverse('store') + '?canceled=1'),
        metadata={'transaction_id': transaction.pk}
    )
    transaction.stripe_session_id = checkout_session.id
    transaction.amount = checkout_session.amount_total
    transaction.save()
    return redirect(checkout_session.url, code=303)
