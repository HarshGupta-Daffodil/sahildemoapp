from django.conf.urls import url
from sample_app.Skill import views

urlpatterns = [
    url(r'^$', views.SkillList.as_view()),
    url(r'^(?P<pk>\d)/$', views.GetSkill.as_view()),
    url(r'^delete/(?P<pk>\d)/$', views.DeleteSkill.as_view()),
    url(r'^update/(?P<pk>\d)/$', views.UpdateSkill.as_view()),
    url(r'^create', views.CreateSkill.as_view())
]