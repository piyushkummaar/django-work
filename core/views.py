from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def main(request):
    return HttpResponse("Hello There!!")

class Home(View):
    def __init__(self):
        self.data = "hellor there"
        self.title = "Hello There it nice you reached here!!"

    def get(self, request,*args,**kwargs):
        return render(request,"home.html",context={"title":self.title,"get_data":self.data})
    def post(self, request,*args,**kwargs):
        print(request.GET)
        return render(request,"home.html",context={"title":self.title,"get_data":self.data})

