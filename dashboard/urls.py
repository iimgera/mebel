from django.urls import path
from dashboard.views import *



urlpatterns = [
    path('', index, name='index'),
    path('customer/list', CustomerListView.as_view(), name='customer-list'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('employee/list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),


]