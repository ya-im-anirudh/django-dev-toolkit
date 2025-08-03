from django.urls import path, include
from dev_toolkit.apps.db_connection_mapper import views
app_name = 'db_connection_mapper'

urlpatterns = [
    path('', views.DBConnectionMapperView.as_view(), name='db_connection_mapper_view'),
]
