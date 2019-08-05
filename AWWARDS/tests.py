from django.test import TestCase

from .models import Profile,Projects,RateReview
import datetime as dt

class ProfileTest(TestCase):
    """class for testing the class Profile."""
    def setUp(self):
        self.peter = Profile(profile_picture = 'Test Image',bio = 'Test',contact = 'Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.peter,Profile))

    def test_save(self):
        self.peter.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile) >0 )

class ProjectsTest(TestCase):
    """Test class to test the class Project."""
    def setUp(self):
        self.peter = Profile(prof_pic = 'Test Image',bio = 'Test',contact = 'Test')
        self.peter.save_profile()

        self.new_project=Projects(profile = self.peter, title = 'Test', image = 'Test Image', description = 'Test', link = 'Test')

    def tearDown(self):
        Profile.objects.all().delete()
        RateReview.objects.all().delete()
        Projects.objects.all().delete()

    def test_save(self):
        self.new_project.save_project()
        projects=Projects.objects.all()
        self.assertTrue(len(projects) >0 )

class RateReviewTest(TestCase):
    """A class to test the Review class methods"""
    def setUp(self):
        self.peter = Profile(profile_picture = 'Test Image',bio = 'Test',contact = 'Test')
        self.peter.save_profile()

        self.project = Projects(profile = self.peter, title = 'Test', image = 'Test Image', description = 'Test', link = 'Test')
        self.project.save()

        self.review = RateReview(project = self.project, design = 4, usability = 4, content = 1)

    def test_save(self):
        self.ratereview.save_ratereview()
        ratereview = Projects.objects.all()
        self.assertTrue(len(ratereview) >0 )