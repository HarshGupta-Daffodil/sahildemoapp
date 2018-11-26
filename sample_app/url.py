from django.conf.urls import url, include
from sample_app.skill import views
from sample_app.department import views as Departmentviews
from sample_app.manager import views as managerviews
from sample_app.employee import views as Employee_view

urlpatterns = [
    url(r'^skills/', include('sample_app.skill.urls')),
    
    url(r'^department/', include('sample_app.department.urls') ),

    url(r'^manager/', include('sample_app.manager.urls') ),
   
    url(r'^Employee/', include('sample_app.employee.urls')),
]