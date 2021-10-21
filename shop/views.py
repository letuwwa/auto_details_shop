from django.shortcuts import render, get_object_or_404

from shop.models import Detail, Category


def home(request):
    details = Detail.objects.all()
    categories = Category.objects.all()

    context_dict = {
        "details": details,
        "categories": categories,
    }
    return render(request, "base.html", context=context_dict)


def details_by_category(request, category_id: int):
    details_in_category = Detail.objects.all().filter(category_id=category_id)
    category = get_object_or_404(Category, id=category_id)

    context_dict = {
        "details": details_in_category,
        "category": category,
    }
    return render(request, "shop/category_details.html", context=context_dict)
