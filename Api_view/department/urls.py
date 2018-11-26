from django.conf.urls import url
from Api_view.department import views as department_view

urlpatterns = [
    
    url(r'^List/$', department_view.DepartmentView.as_view()),
    url(r'^(?P<pk>\d+)/$', department_view. UpdateDepartment.as_view())
]
