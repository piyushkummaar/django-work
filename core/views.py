from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def main(request):
    return HttpResponse("Hello There!!")

class Home(View):
    def get(self, request):
        data = "hellor there"
        title = "Hello There it nice you reached here!!"
        return render(request,"home.html",context={"title":title,"get_data":data})
        
    def post(self, request):
        pass