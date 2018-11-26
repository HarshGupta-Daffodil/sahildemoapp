from django.conf.urls import url
from Api_view.manager import views

urlpatterns = [
    url(r'^/', views. ManagerView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.UpdateManager.as_view())
]