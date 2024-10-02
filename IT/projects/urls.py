from django.urls import path
from .views import projectsview,projectadd,editproject,deleteproject,projectdetailview
app_name = 'project'
urlpatterns = [
    path('',projectsview,name='projects'),
    path('project-add/',projectadd,name='project_add'),
    path('project-edit/<uuid:id>',editproject,name='project_edit'),
    path('project-delete/<id>/',deleteproject,name='project_delete'),
    path('project-detail/<id>/',projectdetailview,name='project_details')
]
