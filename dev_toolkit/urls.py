from django.urls import path, include

from dev_toolkit.views import RootRedirectView

urlpatterns = [
    path('', RootRedirectView.as_view(), name='dashboard_redirect'),
    path('dashboard/', include(('dev_toolkit.apps.dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('dummy-api/', include(('dev_toolkit.apps.dummy_api.urls', 'dummy_api'), namespace='dummy_api')),
    path('db-connection-mapper/', include(('dev_toolkit.apps.db_connection_mapper.urls', 'db_connection_mapper'), namespace='db_connection_mapper')),
]