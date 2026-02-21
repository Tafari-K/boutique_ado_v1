from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51T1pRjHsPvh6i8suG68pRO4eefTuVMCEP2Nk7PW7HSY1J4YZtNKfIuoGSb6J4T3ItU99dHm9kxp5k4Rsi4SjF8co00SAnFr8So',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
