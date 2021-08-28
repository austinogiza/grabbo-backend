from django.contrib import admin
from .models import Blog, Comments, Departments, Professional, Career,Contact

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["name", "date"]


class DepartmentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ProfessionalAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("name",)}

class CareerAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Comments)
admin.site.register(Contact)
admin.site.register(Professional,ProfessionalAdmin)
admin.site.register(Career,CareerAdmin)
