from django.db import models
import datetime
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Branch(models.Model):
	branch_name = models.CharField(max_length=50, default ='', unique=True)
	branch_address = models.CharField(max_length=50, default ='')
	b_contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	branch_contact_number = models.CharField(validators=[b_contact_regex], blank=True, max_length=15)
	branch_created = models.DateTimeField(auto_now_add=True)
	branch_updated = models.DateTimeField(auto_now=True)

	def delete(self, *args, **kwargs):
		self.active = False
		self.deleted_date = datetime.now()
		self.save()

	class Meta:
		verbose_name_plural = 'Branches'

	def __str__(self):
		return self.branch_name

class Underwriter(models.Model):
	underwriter_name = models.CharField(max_length=50, default='', unique=True)
	u_contact_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	underwriter_contact_number = models.CharField(validators=[u_contact_regex], blank=True, max_length=15)
	underwriter_created = models.DateTimeField(auto_now_add=True)
	underwriter_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.underwriter_name

class Product(models.Model):
	product_name = models.CharField(max_length=50, unique=True)
	product_limit = models.IntegerField()
	product_price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
	product_selling_price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
	product_price_effectivity_date = models.DateField(default=datetime.date.today)
	product_underwriter = models.ForeignKey(Underwriter)
	product_created = models.DateTimeField(auto_now_add=True)
	product_updated = models.DateTimeField(auto_now=True)

	def clean(self):
		if self.product_price > self.product_selling_price:
			raise ValidationError("Selling price must be greater than the price.")

	def __str__(self):
		return self.product_name

