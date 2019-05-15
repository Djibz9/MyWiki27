from django.urls import path, include
from . import views
from django.conf import settings import settings
from django.conf.urls.static import static


app_name = 'wiki'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('<str:pk>/delete/confirm', views.delete_confirm, name='delete_confirm'),
    path('<str:pk>/delete', views.delete_page, name='delete_page'),
    path('upload/', views.upload_file, name='upload_page'),
    path('<str:pk>/save', views.save_page, name='save_page'),
    path('<str:pk>/edit', views.edit_page, name='edit_page'),
    path('<str:pk>/', views.view_page, name='detail'),
    
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)