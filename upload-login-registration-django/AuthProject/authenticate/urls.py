from django.conf.urls import url
from views import *



urlpatterns = [
	
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^registration/$', Registeration.as_view(), name='registration'),
	url(r'^upload_file/$',UploadFile.as_view(), name = 'upload_file'),	
]