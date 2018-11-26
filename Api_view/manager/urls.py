from django.conf.urls import url
from Api_view.manager import views as manager_view

urlpatterns = [
    url(r'^/', manager_view. ManagerView.as_view()),
    url(r'^(?P<pk>\d+)/$', manager_view.UpdateManager.as_view())
]