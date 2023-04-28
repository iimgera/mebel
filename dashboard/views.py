from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Customer, Employee, Order
from .forms import CustomerForm, EmployeeForm, OrderForm
from django.db.models import Sum

def index(request):
    return render(request, 'base.html')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'

class CustomerCreateView(CreateView):
    template_name = 'customers/customer_create.html'
    model = Customer
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('customer-list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.object
        orders = Order.objects.filter(customer=customer)
        total = orders.aggregate(Sum('product__price'))
        context['orders'] = orders
        context['total'] = total['product__price__sum']
        return context

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'age', 'gender', 'location']
    customer_form = CustomerForm
    template_name='customer_update.html'



class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')
    template_name='customer_delete.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name='emplyee/employee_create.html'
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('employee-list')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.object
        orders = Order.objects.filter(employee=employee)
        total = orders.aggregate(Sum('product__price'))
        context['orders'] = orders
        context['total'] = total['product__price__sum']
        return context


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'age', 'gender', 'location']
    template_name='employee/employee_update.html'



class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')
    template_name='employee/employee_delete.html'

class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'

class OrderCreateView(CreateView):
    template_name = 'order/order_create.html'
    model = Order
    fields = ['product', 'employee', 'customer', 'order_date']
    success_url = reverse_lazy('order-list')

class OrderDetailView(DetailView):
    template_name = 'order/order_detail.html'
    model = Order

class OrderUpdateView(UpdateView):
    template_name = 'order/order_update.html'
    model = Order
    fields =  ['product', 'employee', 'customer', 'date']
    success_url = reverse_lazy('order-list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_delete.html'
    success_url = reverse_lazy('order-list')