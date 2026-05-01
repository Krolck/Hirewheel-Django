from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Cart, CartItem

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
    # Use the 'related_name' from our model to get the cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})