from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.exam),
    path('trips/new', views.add_trip),
    path('add_exam', views.add_exam),
    path('trips/edit/<int:ID>', views.render_edit_exam),
    path('update', views.update_exam),
    path('delete/<int:uuid>', views.delete_exam),
    path('trips/<int:ID>', views.exam_info),
]