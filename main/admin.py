from django.contrib import admin
from .models import *


admin.site.register(DysonModel)
admin.site.register(OrderModel)
admin.site.register(OrderDysonModel)

