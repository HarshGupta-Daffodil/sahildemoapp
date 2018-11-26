from django.conf.urls import url
from sample_app.Employee import views 

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view()),
    url(r'^(?P<pk>\d)/$', views.GetEmployee.as_view()),
    url(r'^delete/(?P<pk>\d)/$', views.DeleteEmployee.as_view()),
    url(r'^update/(?P<pk>\d)/$', views.UpdateEmployee.as_view()),
    url(r'^create', views.CreateEmployee.as_view())
]