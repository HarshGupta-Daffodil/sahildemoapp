from django.conf.urls import url
from Api_view.department import views 

urlpatterns = [
    url(r'^List/$', views.DepartmentView.as_view()),
    url(r'^(?P<pk>\d+)/$', views. UpdateDepartment.as_view())
]
