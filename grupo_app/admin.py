from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group

from grupo_app.models import Utilisateur, CouponCode

admin.site.register(Utilisateur)
admin.site.register(CouponCode)
