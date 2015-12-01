from django.contrib import admin
from insurance.models import Branch, Underwriter, Product

class ProductCreatedAndUpdated(admin.ModelAdmin):
	list_display = ("__str__", "product_created", "product_updated")

class BranchCreatedAndUpdated(admin.ModelAdmin):
	list_display = ("__str__", "branch_created", "branch_updated")

class UnderwriterCreatedAndUpdated(admin.ModelAdmin):
	list_display = ("__str__", "underwriter_created", "underwriter_updated")

admin.site.register(Branch, BranchCreatedAndUpdated)
admin.site.register(Underwriter, UnderwriterCreatedAndUpdated)
admin.site.register(Product, ProductCreatedAndUpdated)