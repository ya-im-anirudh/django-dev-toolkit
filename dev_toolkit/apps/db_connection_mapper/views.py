from django.core.exceptions import ImproperlyConfigured
from django.db.models import ForeignKey, ManyToManyField, OneToOneField
from django.views.generic.base import TemplateResponseMixin
from django.views import View
from django.apps import apps
class DBConnectionMapperView(TemplateResponseMixin, View):
    template_base_path = "dev_toolkit/database_mapper/"
    template_view = "dashboard_connection_view.html"

    def get_template_names(self):
        if self.template_view:
            return [self.template_base_path + self.template_view]
        raise ImproperlyConfigured("No template_view set.")

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):

        """Prepare context data for the view."""

        all_models = apps.get_models()
        print(all_models)

        model_list = []
        for model in all_models:
            fields_data = []
            for field in model._meta.get_fields():
                # Skip auto-generated reverse relations if not needed
                if field.auto_created and not field.concrete:
                    continue

                is_relation = isinstance(field, (ForeignKey, ManyToManyField, OneToOneField))
                related_model = None
                if is_relation and hasattr(field, 'related_model') and field.related_model:
                    related_model = {
                        'app_label': field.related_model._meta.app_label,
                        'model_name': field.related_model._meta.model_name,
                        'verbose_name': field.related_model._meta.verbose_name.title()
                    }

                fields_data.append({
                    'name': field.name,
                    'field_type': field.get_internal_type() if hasattr(field, 'get_internal_type') else type(
                        field).__name__,
                    'is_relation': is_relation,
                    'related_model': related_model,
                })

            model_list.append({
                'app_label': model._meta.app_label,
                'model_name': model._meta.model_name,
                'verbose_name': model._meta.verbose_name.title(),
                'fields': fields_data
            })

        context = {'db_models': model_list}
        context.update(kwargs)
        # Add any additional context here
        return context
