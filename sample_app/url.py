from django.conf.urls import url
from sample_app.skill import views
from sample_app.department import views as Departmentviews
from sample_app.manager import views as managerviews
from sample_app.employee import views as Employee_view

urlpatterns = [
    url(r'^skills/$', views.SkillList.as_view()),
    url(r'^skill/(?P<pk>\d)/$', views.GetSkill.as_view()),
    url(r'^skill/delete/(?P<pk>\d)/$', views.DeleteSkill.as_view()),
    url(r'^skill/update/(?P<pk>\d)/$', views.UpdateSkill.as_view()),
    url(r'^skill/create', views.CreateSkill.as_view()),

    url(r'^department/$', Departmentviews.DepartmentList.as_view()),
    url(r'^department/(?P<pk>\d)/$', Departmentviews.GetDepartment.as_view()),
    url(r'^department/delete/(?P<pk>\d)/$', Departmentviews.DeleteDepartment.as_view()),
    url(r'^department/update/(?P<pk>\d)/$', Departmentviews.UpdateDepartment.as_view()),
    url(r'^department/create', Departmentviews.CreateDepartment.as_view()),

    url(r'^manager/$', managerviews.ManagerList.as_view()),
    url(r'^manager/(?P<pk>\d)/$', managerviews.GetManager.as_view()),
    url(r'^manager/delete/(?P<pk>\d)/$', managerviews.DeleteManager.as_view()),
    url(r'^manager/update/(?P<pk>\d)/$', managerviews.UpdateManager.as_view()),
    url(r'^manager/create', managerviews.CreateManager.as_view()),

    url(r'^Employee/$', Employee_view.EmployeeList.as_view()),
    url(r'^Employee/(?P<pk>\d)/$', Employee_view.GetEmployee.as_view()),
    url(r'^Employee/delete/(?P<pk>\d)/$', Employee_view.DeleteEmployee.as_view()),
    url(r'^Employee/update/(?P<pk>\d)/$', Employee_view.UpdateEmployee.as_view()),
    url(r'^Employee/create', Employee_view.CreateEmployee.as_view())
]