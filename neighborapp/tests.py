from django.test import TestCase
from .models import Post,Profile,Neighborhood,Business
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='joan',password='wueh')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestBusiness(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='joan',password='wueh')
        self.business = Business.create(id=1,name='jamhuri',email='joan.kirui@student.moringaschool.com',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_post(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)


    def test_search_by_name(self):
        self.business.save()
        business = Business.search_by_name('test')
        self.assertTrue(len(business) > 0)

class TestPost(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=2, username='joan',password='wueh')
        self.post = Post.objects.create(id=2,title='test-post',user=self.user,post='farming')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

class TestNeighborhood(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=2, username='joan',password='wueh')
        self.neighborhood = Neighborhood.objects.create(id=1,name='hood',location='naromoru',health_tell='0798',police_number='556')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_create_neighborhood(self):
        self.neighborhood.save()

    def test_delete_neighborhood(self):
        self.neighborhood.delete()

    def test_find_neighborhood(self):
        self.neighborhood.save()
        neighborhood = Neighborhood.find_neighborhood('tesr')
        self.assertTrue(len(neighborhood) > 0)

