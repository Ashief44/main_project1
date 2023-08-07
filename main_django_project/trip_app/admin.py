from django.contrib import admin
from.models import Destination
from.models import Detailed_desc
from.models import  passanger_detail
from.models import Card
from.models import NetBanking
from.models import  Transaction

# Register your models here.
admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(passanger_detail)
admin.site.register(Card)
admin.site.register(NetBanking)
admin.site.register( Transaction)
