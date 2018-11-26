from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^skills_api/', include("Api_view.skill.urls")),
    url(r'^department_api/', include("Api_view.department.urls")),
    url(r'^manager_api/', include("Api_view.manager.urls")),
    url(r'^Employee_api/', include("Api_view.employee.urls")),
]
