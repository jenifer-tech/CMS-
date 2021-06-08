from django.contrib import admin
from django.db.models.base import Model
from account.models import Account

admin.site.register(Account)
