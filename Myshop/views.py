from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, UpdateView
from django.views.generic.edit import DeleteView
from haystack.query import SearchQuerySet

from .models import *
from .forms import *


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_public=True)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_details.html'


class ProductDelete(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = '/'
    context_object_name = 'product'

    success_message = "Record deleted Successfully."

    # this func for protecting the view for 'admin' access only, and to use it inherit UserPassesTestMixin at the leftmost position of your view.
    def test_func(self):
        return self.request.user.username.startswith('admin')


class ProductUpdate(UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    # this func for protecting the view for 'admin' access only, and to use it inherit UserPassesTestMixin at the leftmost position of your view.
    def test_func(self):
        return self.request.user.username.startswith('admin')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        super(ProductUpdate, self).form_valid(form)
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        print("------------INVALID FORM----------------")
        return super(ProductUpdate, self).form_invalid(form)


class AddProduct(UserPassesTestMixin, View):
    model = Product
    form_class = ProductForm
    template_name = 'new_product.html'

    # this func for protecting the view for 'admin' access only, and to use it inherit UserPassesTestMixin at the leftmost position of your view.
    def test_func(self):
        return self.request.user.username.startswith('admin')

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(self.request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST' and self.request.is_ajax():
            form = ProductForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                product = form.save()
                product.image = request.FILES['image']
                form.save()
                return JsonResponse({'status': "Save"}, status=200)
        return JsonResponse({'status': "Error"}, status=400)

# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# def admin_check(user):
#     return user.username.startswith('admin')
#
# @user_passes_test(admin_check)
# ----------- Alternative Code of admin check method above ------------------------
# @user_passes_test(lambda user: user.is_superuser)
#  def add_product(request):
#      form = ProductForm()
#      if request.method == 'POST':
#          form = ProductForm(request.POST, request.FILES)
#          if form.is_valid():
#              title = request.POST['title']
#              product = form.save()
#              product.image = request.FILES['image']
#              form.save()
#              # file_type = product.image.url.split('.')[-1]
#              # file_type = file_type.lower()
#              # if file_type not in IMAGE_FILE_TYPES:
#              #     return render(request, 'profile_maker/error.html')
#
#              return JsonResponse({'status': "Save"})
#              # return redirect('product_detail', pk=product.pk)
#              # return redirect('new_product')
#
#      context = {"form": form}
#      return render(request, 'new_product.html', context)


class SearchResults(ListView):
    model = Product
    template_name = 'search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.result = self.request.GET.get('query')
        return SearchQuerySet().filter(text=self.result)
