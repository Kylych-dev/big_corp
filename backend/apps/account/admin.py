from django.contrib import admin

from .models import (
    CustomUser,
    UserProfile,
    ManagerProfile
)


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(ManagerProfile)
