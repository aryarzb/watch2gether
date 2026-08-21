from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import user


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        languages = request.POST.getlist("languages")
        if not languages:
            languages = ["english"]
        if password != confirm_password:
            return render(
                request,
                "users/register.html",
                {"error": "Passwords do not match."}
            )
        new_user = user.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            username=username,
            password=password,
            languages=languages
        )
        return redirect("sign_in")
    return render(request, "users/register.html")



def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "show/home.html")
    return render(request, "show/home.html")