from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(HomeView, self).get_queryset()
        return queryset.filter(is_public=True)


# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

@login_required
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = request.FILES['image']
            # file_type = product.image.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     return render(request, 'profile_maker/error.html')
            product.save()

            # return JsonResponse({'status': "Save"})
            # return redirect('product_detail', pk=product.pk)
            return redirect('new_product')

    context = {"form": form}
    return render(request, 'new_product.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_details.html'
