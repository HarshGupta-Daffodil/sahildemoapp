from django.conf.urls import url, include


urlpatterns = [
    url(r'^skills/', include('sample_app.Skill.urls')),
    
    url(r'^department/', include('sample_app.Department.urls') ),

    url(r'^manager/', include('sample_app.Manager.urls') ),
   
    url(r'^Employee/', include('sample_app.Employee.urls')),
]