from django.urls import path
from . import views


urlpatterns = [
    path('', views.notes_list, name="notes_list"),
    path('<int:pk>', views.note_details, name="note_details"),
    path('<int:pk>/ViewPdf', views.NoteViewPdf, name='note_view_pdf'),
    path('<int:pk>/getPdf',views.NoteGetPdf, name='note_get_pdf'),
    path('add_note/', views.add_note, name='add_note'),
    path('update_note/<int:pk>', views.update_note, name='update_note'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('delete_all_notes/', views.delete_all_notes, name='delete_all_notes'),
    path('notes_list_today/', views.notes_list_today, name='notes_list_today'),
    path('notes_this_week/', views.notes_this_week, name='notes_this_week'),
    path('notes_this_month/', views.notes_this_month, name='notes_this_month'),
    path('notes_this_year/', views.notes_this_year, name='notes_this_year')
]

