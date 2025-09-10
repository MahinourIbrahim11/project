from django.shortcuts import render
from .models import Form
from .forms import LoginForm

# Create your views here.
def home(request):
    x={'name': 'mahinour', 'age': 20}
    return render(request, 'pages/home.html', x)

def about(request):
    return render(request, 'pages/about.html')


def form_view(request):
    if request.method == 'POST':
        Lf = LoginForm(request.POST)
        if Lf.is_valid():
            Lf.save()

    return render(request, 'pages/form.html', {'Lf': LoginForm()})