from django.test import TestCase
from insurance.models import Branch, Underwriter

class BranchModelTest(TestCase):
	def test_creating_new_branch(self):
		branch = Branch ()
		branch.branch_name = "Cebuana"

		branch.save()

		all_branch_in_database = Branch.objects.all()
		self.assertEqual(len(all_branch_in_database), 1)
		only_branch_in_database = all_branch_in_database[0]
		self.assertEquals(only_branch_in_database, branch)

		self.assertEquals(only_branch_in_database.name, "Cebuana")

	def test_creating_new_underwriter(self):
		uderwriter = Underwriter ()
		underwriter.underwriter_name = "Sun Life of Canada"

		underwriter.save()

	def test_creating_new_product(self):
		pass

