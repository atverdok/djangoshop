from django.urls import reverse
from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreatedForm
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
            # return render(request,
            #               'orders/order/created.html',
            #               locals())
    else:
        form = OrderCreatedForm()
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})
