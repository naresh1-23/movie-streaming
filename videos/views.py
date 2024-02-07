from django.shortcuts import render
from django.views import View
from .models import Videos

class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        videos = Videos.objects.all()
        for i in videos:
            print(i.thumbnail.url)
        return render(request, self.template_name, {"videos": videos})
        