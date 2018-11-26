from django.conf.urls import url
from sample_app.Manager import views

urlpatterns = [
    url(r'^$', views.ManagerList.as_view()),
    url(r'^(?P<pk>\d)/$', views.GetManager.as_view()),
    url(r'^delete/(?P<pk>\d)/$', views.DeleteManager.as_view()),
    url(r'^update/(?P<pk>\d)/$', views.UpdateManager.as_view()),
    url(r'^create', views.CreateManager.as_view())
]