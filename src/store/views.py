from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Item, Cart, CartItem

def store(request):

    if request.user.is_authenticated:
        items = Item.objects.all()
        return render(request, 'store/store.html', {'items': items})
    return render(request, 'home.html')




# def add_to_cart(request, item_id):
#     product = get_object_or_404(Item, id=item_id)
    

#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#     else:
#         cart_id = request.session.get('cart_id')
#         if cart_id:
#             cart = Cart.objects.filter(id=cart_id, user=None).first()
#             if not cart: 
#                 cart = Cart.objects.create(user=None)
#         else:
#             cart = Cart.objects.create(user=None)
#             request.session['cart_id'] = cart.id


#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart, 
#         product=product,
#         defaults={'price': product.price}
#     )
    
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect('cart_detail')