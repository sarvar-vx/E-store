from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def home_page(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.select_related('category').all().order_by('-created_at')

    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=active_category)

    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category,
        'query': query,
    }
    return render(request, 'index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('category'), pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)