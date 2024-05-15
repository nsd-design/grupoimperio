from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from grupo_app.forms import RegisterForm, LoginForm, CouponCodeForm
from grupo_app.models import Utilisateur, CouponCode

temp_path = "grupo_app/pages/"


def login_user(request):
    login_form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Vous êtes connecté avec succès !")
                print("Vous êtes connecté avec succès !")
                return redirect("payment")

    return render(request, temp_path+"login.html", {"form": login_form})


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        print("register posted...")
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if len(password) < 8:
                return messages.error(request, "Les mots de passe doivent contenir au moins 8 caratères")

            if password == confirm_password:
                lastname = request.POST['lastname']
                firstname = form.cleaned_data['firstname']
                adr_email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                try:
                    new_user = Utilisateur.objects.create_user(
                        username=username, last_name=lastname, first_name=firstname,
                        email=adr_email, password=password
                    )
                except Exception as e:
                    print(e)
                else:
                    new_user.save()
                    print("user saved!")
    return render(request, temp_path+"register.html", {"form": form})


# @login_required(login_url="login")
def payment(request):
    form = CouponCodeForm()
    if request.method == "POST":
        coupon_form = CouponCodeForm(request.POST)
        if coupon_form.is_valid():
            coupon = coupon_form.cleaned_data["coupon"]
            coupon_type = request.POST.get('type')

            if coupon_type is None:
                return JsonResponse({"errors": True,
                                     "msg": "Une erreur s'est produite lors de la verification du coupon"}
                                    )

            coupon_type = int(coupon_type)

            instance = CouponCode.objects.create(
                coupon=coupon,
                coupon_type=coupon_type,
                created_by=request.user
            )
            instance.save()
            return JsonResponse({"success": True, "msg": "Abonnement effectué avec succès !"})
        else:
            return JsonResponse({"errors": True, "msg": coupon_form.errors})

    context = {"form": form}
    return render(request, temp_path+"payment.html", context)
