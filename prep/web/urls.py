from django.urls import path, include

from prep.web import views

urlpatterns = [
	path('', views.index, name='index'),
	path('album/add', views.add_album, name='add-album'),
	path('album/details/<int:pk>', views.album_details, name='album-details'),
	path('album/edit/<int:pk>', views.edit_album, name='edit-album'),
	path('album/delete/<int:pk>', views.delete_album, name='delete-album'),
	path('profile/details/', views.profile_details, name='profile-details'),
	path('profile/delete/', views.profile_delete, name='profile-delete'),
]