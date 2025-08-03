from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.db import connection

from django.views.generic import RedirectView
from django.urls import reverse_lazy

class RootRedirectView(RedirectView):
    url = reverse_lazy('dashboard:dashboard_view')  # Use your dashboard view name here


@login_required
@user_passes_test(lambda u: u.is_staff)
def dev_toolkit_dashboard_view(request):

    return render(request, 'dev_toolkit/dashboard_view.html')






@login_required
@user_passes_test(lambda u: u.is_staff)
def dummy_api_list_view(request):
    """
    Renders the main API tester page and provides a list of all installed models.
    """
    # Get all installed models
    all_models = apps.get_models()

    # Format models for the template's dropdown
    model_list = []
    for model in all_models:
        model_list.append({
            'app_label': model._meta.app_label,
            'model_name': model._meta.model_name,
            'verbose_name': model._meta.verbose_name.title(),
        })

    context = {
        'models': sorted(model_list, key=lambda x: x['app_label'])
    }
    return render(request, 'dev_toolkit/dummy_api/list_view.html', context)


def db_mapper_view(request):
    """
    Renders the HTML template for the database mapper.
    """
    return render(request, 'dev_toolkit/database_mapper/dashboard_connection_view.html')


def get_db_schema(request):
    """
    Introspects the Django database and returns the schema as a JSON object.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET requests are supported'}, status=405)

    nodes = []
    links = []

    try:
        cursor = connection.cursor()

        # Get all table names in the database
        table_list = connection.introspection.get_table_list(cursor)

        table_names = [table.name for table in table_list]

        for table_name in table_names:
            # Get fields for each table
            table_description = connection.introspection.get_table_description(cursor, table_name)
            fields = [f"{desc.name}: {desc.display_size}" for desc in table_description]
            nodes.append({
                'id': table_name,
                'fields': fields
            })

            # Get foreign key relationships
            # Note: This method is a simplified introspection for demonstration.
            # It might not capture all relationship types.
            try:
                relations = connection.introspection.get_relations(cursor, table_name)
                for field_index, (target_col_index, target_table_name) in relations.items():
                    source_field_name = table_description[field_index].name
                    target_field_name = connection.introspection.get_table_description(cursor, target_table_name)[
                        target_col_index].name

                    links.append({
                        'source': table_name,
                        'target': target_table_name,
                        'source_field': source_field_name,
                        'target_field': target_field_name,
                    })
            except connection.DatabaseError:
                # Some databases might not support introspection of relationships directly.
                pass

    except Exception as e:
        return JsonResponse({'error': f'Failed to introspect database: {str(e)}'}, status=500)

    # Prepare the final schema data
    schema_data = {
        'nodes': nodes,
        'links': links
    }

    return JsonResponse(schema_data)


@login_required
@user_passes_test(lambda u: u.is_staff)
def view_db(request):
    return render(request, 'dev_toolkit/database_mapper/dashboard_connection_view.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def dummy_api_tester_view(request):
    """
    Renders the main API tester page and provides a list of all installed models.
    """
    # Get all installed models
    all_models = apps.get_models()

    # Format models for the template's dropdown
    model_list = []
    for model in all_models:
        model_list.append({
            'app_label': model._meta.app_label,
            'model_name': model._meta.model_name,
            'verbose_name': model._meta.verbose_name.title(),
        })

    context = {
        'models': sorted(model_list, key=lambda x: x['app_label'])
    }
    return render(request, 'dev_toolkit/dummy_api/create_view.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def get_model_details(request):
    """
    An AJAX endpoint to fetch fields and relationships for a selected model.
    """
    app_label = request.GET.get('app_label')
    model_name = request.GET.get('model_name')

    if not app_label or not model_name:
        return JsonResponse({'error': 'Missing model information'}, status=400)

    try:
        model = apps.get_model(app_label, model_name)
    except LookupError:
        return JsonResponse({'error': 'Model not found'}, status=404)

    fields = []
    relations = []

    for field in model._meta.get_fields():
        if isinstance(field, (ForeignKey, ManyToManyField, OneToOneField)):
            # It's a relational field
            relations.append({
                'name': field.name,
                'type': field.get_internal_type(),
                'related_model': field.related_model._meta.model_name,
                'related_app': field.related_model._meta.app_label,
            })
        else:
            # It's a standard data field
            # We avoid adding the reverse side of relations here
            if not field.auto_created:
                fields.append({
                    'name': field.name,
                    'type': field.get_internal_type(),
                })

    return JsonResponse({'fields': fields, 'relations': relations})