from django.conf.urls import url
from Api_view.skill import views

urlpatterns = [
    url(r'^$', views.SkillView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.UpdateSkill.as_view())
]