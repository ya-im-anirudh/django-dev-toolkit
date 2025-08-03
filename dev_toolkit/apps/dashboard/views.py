from django.core.exceptions import ImproperlyConfigured
from django.views.generic.base import TemplateResponseMixin
from django.views import View

class DashboardView(TemplateResponseMixin, View):
    template_base_path = "dev_toolkit/"
    template_view = "dashboard_view.html"

    def get_template_names(self):
        if self.template_view:
            return [self.template_base_path + self.template_view]
        raise ImproperlyConfigured("No template_view set.")

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = {}
        context.update(kwargs)
        # Add any additional context here
        return context
