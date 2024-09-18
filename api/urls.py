from django.urls import path
from . import views

urlpatterns = [
    path("", views.getCustomers),
    path("add/", views.addCustomer),
    path("", views.getOrders),
    path("add/", views.addOrder)
]
