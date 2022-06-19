from django.contrib import admin
from .models import Jobs, References, Skills, Roles, Works, Education, Objectives, Address, Details, Duties

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Duties)
admin.site.register(Details)
admin.site.register(Address)
admin.site.register(References)
admin.site.register(Skills)
admin.site.register(Roles)
admin.site.register(Works)
admin.site.register(Education)
admin.site.register(Objectives)
