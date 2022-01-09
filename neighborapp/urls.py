from django.urls import path
from django.contrib import admin
from .import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index, name='index'),
    path('profile/',views.profile, name='profile'),
    path('update/',views.edit_profile, name='edit'),
    path('members/<hood_id>', views.hood_members, name='members'),
    path('new-hood/', views.newhood, name='newhood'),
    path('newpost/<hood_id>', views.make_post, name='makepost'),
    # path('singlehood/', views.single_hood, name='singlehood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('join_hood/<id>', views.join_hood, name='join_hood'),
    path('leave_hood/<id>', views.leave_hood,name='leave_hood'),
    path('search',views.search_business, name='search_business')

]
if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)