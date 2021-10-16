from django.shortcuts import render

from shop.models import Detail, Category


def home(request):
    details = Detail.objects.all()
    categories = Category.objects.all()

    context_dict = {
        "details": details,
        "categories": categories,
    }
    return render(request, "base.html", context=context_dict)
