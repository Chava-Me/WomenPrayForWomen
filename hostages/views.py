from django.http import HttpResponse


def new_page(request):
    return HttpResponse('New Product')

