from django.shortcuts import render,get_object_or_404


from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'home.html'
