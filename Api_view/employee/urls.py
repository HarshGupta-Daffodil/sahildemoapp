from django.conf.urls import url
from Api_view.employee import views

urlpatterns = [
    url(r'^$', views.EmployeeView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.UpdateEployee.as_view()),
]
