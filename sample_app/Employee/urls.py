from django.conf.urls import url
from sample_app.Employee import views as Employee_view

urlpatterns = [
    url(r'^$', Employee_view.EmployeeList.as_view()),
    url(r'^(?P<pk>\d)/$', Employee_view.GetEmployee.as_view()),
    url(r'^delete/(?P<pk>\d)/$', Employee_view.DeleteEmployee.as_view()),
    url(r'^update/(?P<pk>\d)/$', Employee_view.UpdateEmployee.as_view()),
    url(r'^create', Employee_view.CreateEmployee.as_view())
]