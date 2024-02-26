from django.shortcuts import render


# Create your views here.
def index(request):
    template_name = "index-7.html"
    # context ={
    #     "is_index" : True,
    # }
    return render(request, template_name)