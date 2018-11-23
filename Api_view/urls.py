from django.conf.urls import url
from Api_view.skill import views
from Api_view.department import views as department_view
from Api_view.manager import views as manager_view
from Api_view.employee import views as employee_view

urlpatterns = [
    url(r'^skills_api/$', views.SkillView.as_view()),
    url(r'^skill_api/(?P<pk>\d+)/$', views.UpdateSkill.as_view()),
    url(r'^department_api/$', department_view.DepartmentView.as_view()),
    url(r'^departments_api/(?P<pk>\d+)/$', department_view. UpdateDepartment.as_view()),
    url(r'^manager_api/$', manager_view. ManagerView.as_view()),
    url(r'^manager_api/(?P<pk>\d+)/$', manager_view.UpdateManager.as_view()),
    url(r'^Employee_api/$', employee_view.EmployeeView.as_view()),
    url(r'^Employee_api/(?P<pk>\d+)/$', employee_view.UpdateEployee.as_view()),
]
