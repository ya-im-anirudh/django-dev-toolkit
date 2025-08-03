from django.urls import path, include
from dev_toolkit.apps.dummy_api import views
from dev_toolkit.apps.dummy_api.views import DummyAPIView, DummyApiRedirectView

app_name = 'dummy_api'

urlpatterns = [
    path('', DummyApiRedirectView.as_view()),
    path('<str:view_type>/', DummyAPIView.as_view(), name='dummy_api_dynamic'),
]
