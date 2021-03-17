from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView
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


@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

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


# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

@login_required
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            product.image = request.FILES['image']
            # file_type = product.image.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     return render(request, 'profile_maker/error.html')

            # return JsonResponse({'status': "Save"})
            # return redirect('product_detail', pk=product.pk)
            return redirect('new_product')

    context = {"form": form}
    return render(request, 'new_product.html', context)
