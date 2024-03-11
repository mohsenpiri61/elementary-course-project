from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup_view(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)
    else:
        return redirect('/')
