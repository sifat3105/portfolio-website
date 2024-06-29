from django.shortcuts import render, redirect
from .forms import AboutForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def about_create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your success page URL name
    else:
        form = AboutForm()
    return render(request, 'about_create.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')
