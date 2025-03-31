from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

# Create your views here.

def thanks(request, order_id):
    """Handles the thank you page after an order is placed."""
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'thanks.html', {'customer_order': customer_order})


class orderHistory(LoginRequiredMixin, View):
    """Displays the order history for a logged-in user."""
    def get(self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Order.objects.filter(emailAddress=email)
            # Added debug print statement for clarity
            print(f"Orders retrieved for {email}: {order_details}")
        return render(request, 'order_list.html', {'order_details': order_details})


class orderDetail(LoginRequiredMixin, View):
    """Displays the details of a specific order for a logged-in user."""
    def get(self, request, order_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order = Order.objects.get(id=order_id, emailAddress=email)
            order_items = OrderItem.objects.filter(order=order)
        return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})