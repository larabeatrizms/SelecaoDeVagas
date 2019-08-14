from django.urls import path
from .views import *

# CRUD - CREATE, READ, UPDATE, DELETE

"""
urlpatterns = [
    path('', list_cargos, name='list_cargos'),
    path('new', create_cargo, name='create_cargo'),
    path('update/<int:id>/', update_cargo, name='update_cargo'),
    path('delete/<int:id>/', delete_cargo, name='delete_cargo'),
]
"""

urlpatterns = [
    path('', list_candidatos, name='list_candidatos'),
    path('new', create_candidato, name='create_candidato'),
    path('update/<int:id>/', update_candidato, name='update_candidato'),
    path('delete/<int:id>/', delete_candidato, name='delete_candidato'),
]
