from django.shortcuts import render
from django.views import View
from .models import Videos
from django.views.generic.detail import DetailView

class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        # if not request.user.is_authenticated:
        #     return redirect("")
        videos = Videos.objects.all()
        for i in videos:
            print(i.thumbnail.url)
        return render(request, self.template_name, {"videos": videos})
        
class MovieView(DetailView):
    model = Videos
    template_name = "movie.html"
    context_object_name = 'video'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["other_movies"] = Videos.objects.exclude(id = self.kwargs["pk"])
        print(context)
        return context
    