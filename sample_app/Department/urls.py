from django.conf.urls import url
from sample_app.Department import views as Departmentviews

urlpatterns = [
    url(r'^$', Departmentviews.DepartmentList.as_view()),
    url(r'^(?P<pk>\d)/$', Departmentviews.GetDepartment.as_view()),
    url(r'^delete/(?P<pk>\d)/$', Departmentviews.DeleteDepartment.as_view()),
    url(r'^update/(?P<pk>\d)/$', Departmentviews.UpdateDepartment.as_view()),
    url(r'^create', Departmentviews.CreateDepartment.as_view()),
]