from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def Home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            message=message
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("home")

    return render(request, "home.html")