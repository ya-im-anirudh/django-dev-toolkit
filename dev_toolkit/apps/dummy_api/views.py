from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.views.generic.base import TemplateResponseMixin
from django.views import View
from django.views.generic import RedirectView
from django.urls import reverse_lazy

class DummyApiRedirectView(RedirectView):
    pattern_name = 'dummy_api:dummy_api_dynamic'
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(view_type='list')

class DummyAPIView(TemplateResponseMixin, View):
    template_base_path = "dev_toolkit/dummy_api/"
    template_name = None

    def get_template_names(self):
        view_type = self.kwargs.get('view_type')
        if view_type == 'list':
            return [self.template_base_path + 'list_view.html']
        elif view_type == 'create':
            return [self.template_base_path + 'create_view.html']
        else:
            raise ImproperlyConfigured(f"Unknown view type: {view_type}")

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)