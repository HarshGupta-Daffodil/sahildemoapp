from django.conf.urls import url
from Api_view.employee import views as employee_view

urlpatterns = [
    url(r'^$', employee_view.EmployeeView.as_view()),
    url(r'^(?P<pk>\d+)/$', employee_view.UpdateEployee.as_view()),
]
