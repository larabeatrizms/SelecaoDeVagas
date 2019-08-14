from django.urls import path
from .views import list_cargos, create_cargo, update_cargo, delete_cargo

urlpatterns = [
    path('', list_cargos, name='list_cargos'),
    path('new', create_cargo, name='create_cargo'),
    path('update/<int:id>/', update_cargo, name='update_cargo'),
    path('delete/<int:id>/', delete_cargo, name='delete_cargo'),
]


# CRUD - CREATE, READ, UPDATE, DELETE