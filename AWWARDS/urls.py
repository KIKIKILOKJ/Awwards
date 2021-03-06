from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^projects$',views.projects,name='projects'),
    url(r'^new_projects$',views.upload_projects,name='new_projects'),
    url(r'^search$',views.search_projects,name='search'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^edit_profile$',views.edit_profile,name='edit_profile'),
    url(r'^new_review$',views.review,name='new_review'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    