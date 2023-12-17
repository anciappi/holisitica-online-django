from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from .forms import RegisterForm
from django.views import View
from django.contrib.auth import authenticate, login
    

# PAGINA DE INICIO
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context


# PAGINA DE ABOUT
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context


# PAGINA DE PRICING
class ArancelesView(TemplateView):
    template_name = 'aranceles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context

# PAGINA DE CONTACT
class ContactView(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context

# PAGINA DE TERAPHIST
class teraphistsView(TemplateView):
    template_name = 'terapeutas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context

# PAGINA DE TERAPHY
class TeraphyView(TemplateView):
    template_name = 'terapias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context




#REGISTRO DE USUARIOS
class RegisterView(View):
    def get(self, request):
        data = {
            'form': RegisterForm()
        }

        return render(request, 'registration/register.html', data)
    
    def post(self,request):
        user_creation_form = RegisterForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(
                username=user_creation_form.cleaned_data['username'],
                password=user_creation_form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
        data = {
            'form': user_creation_form
        }
        return render(request, 'registration/login.html')