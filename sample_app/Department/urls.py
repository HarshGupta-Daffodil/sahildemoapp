from django.conf.urls import url
from sample_app.Department import views

urlpatterns = [
    url(r'^$', views.DepartmentList.as_view()),
    url(r'^(?P<pk>\d)/$', views.GetDepartment.as_view()),
    url(r'^delete/(?P<pk>\d)/$', views.DeleteDepartment.as_view()),
    url(r'^update/(?P<pk>\d)/$', views.UpdateDepartment.as_view()),
    url(r'^create', views.CreateDepartment.as_view()),
]