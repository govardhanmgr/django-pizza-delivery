from django.urls import path
from . import views



urlpatterns = [
	# path('',views.HelloOrdersView.as_view(), name="hello_orders"),
	path('',views.OrderCreateListView.as_view(), name="orders"),
    
]