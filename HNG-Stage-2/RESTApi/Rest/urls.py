from . import views
from django.urls import path, re_path, register_converter
from .views import PersonListCreateView, PersonDetailView


class IntOrStrConverter:
    regex = r'\d+|[\w\s]+'

    def to_python(self, value):
        if value.isdigit():
            return int(value)
        return value

    def to_url(self, value):
        if isinstance(value, int):
            return str(value)
        return value

register_converter(IntOrStrConverter, 'int_or_str')

app_name='Rest'
urlpatterns = [
    # creates a new person object
    path('', PersonListCreateView.as_view(), name='Person-create'),
    path('<int_or_str:parameter>/', PersonDetailView.as_view(), name='Person-detail-update-dellete')
    # takes only int ID
    #path('api/<int:id>/', PersonDetailView.as_view(), name='Person-detail-by-id'),
    # takes string parameters only
    #path('api/<str:name>/', PersonDetailView.as_view(), name='Person-detail-by-name'),
]
