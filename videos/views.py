from django.shortcuts import render, redirect
from django.views import View
from .models import Videos
from django.views.generic.detail import DetailView
from django.contrib import messages
from user.models import PaymentDate
from datetime import datetime


class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        if self.request.user.is_authenticated:
            if self.request.user.verified:
                subs = PaymentDate.objects.filter(user = self.request.user).first()
                if subs:    
                    if subs.valid_date < datetime.now().date():
                        subs.delete()
                        self.request.user.verified = False
                        self.request.user.save()
                        messages.warning(request, "Your subscription has ended. Please take subscription again.")
                        return redirect("subscription")
                    videos = Videos.objects.all()
                    return render(request, self.template_name, {"videos": videos})
                else:
                    messages.warning(request, "Please take subscription to access the movies.")
                    return redirect("subscription")
            else:
                messages.warning(request, "Please select a subscription plan")
                return redirect("subscription")
        messages.warning(request, "Please login first")
        return redirect("login")
        
class MovieView(DetailView):
    model = Videos
    template_name = "movie.html"
    context_object_name = 'video'
    
    
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.verified:
                context = super().get_context_data(**kwargs)
                context["other_movies"] = Videos.objects.exclude(id = self.kwargs["pk"])
                print(context)
                return context
            else:
                messages.warning(request, "Please select a subscription plan")
                return redirect("subscription")
        messages.warning(request, "Please login first")
        return redirect("login")
                
    