from django.test import TestCase
from insurance.models import Branch

class BranchModelTest(TestCase):
	def test_creating_new_branch(self):
		branch = Branch ()
		branch.name = "Cebuana"

		branch.save()

		all_branch_in_database = Branch.objects.all()
		self.assertEqual(len(all_branch_in_database), 1)
		only_branch_in_database = all_branch_in_database[0]
		self.assertEquals(only_branch_in_database, branch)

		self.assertEquals(only_branch_in_database.name, "Cebuana")

