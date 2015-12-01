from django.contrib import admin
from insurance.models import Branch, Underwriter, Product

class CreatedAndUpdated(admin.ModelAdmin):
	list_display = ("__str__", "product_created", "product_updated")

admin.site.register(Branch)
admin.site.register(Underwriter)
admin.site.register(Product, CreatedAndUpdated)