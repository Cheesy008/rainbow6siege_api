from django.contrib import admin

from .models import (
    Organization,
    Operator,
)

admin.site.register(Organization)
admin.site.register(Operator)

