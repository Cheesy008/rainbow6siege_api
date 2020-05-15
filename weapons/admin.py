from django.contrib import admin

from .models import (
    Weapon,
    Gadget,
    Attachments,
    Loadout,
)

admin.site.register(Weapon)
admin.site.register(Gadget)
admin.site.register(Attachments)
admin.site.register(Loadout)

