from django.conf.urls import url
from sample_app.Manager import views as managerviews

urlpatterns = [
    url(r'^$', managerviews.ManagerList.as_view()),
    url(r'^(?P<pk>\d)/$', managerviews.GetManager.as_view()),
    url(r'^delete/(?P<pk>\d)/$', managerviews.DeleteManager.as_view()),
    url(r'^update/(?P<pk>\d)/$', managerviews.UpdateManager.as_view()),
    url(r'^create', managerviews.CreateManager.as_view())
]