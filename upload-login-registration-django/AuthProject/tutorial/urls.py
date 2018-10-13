
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_swagger import urls as swag_urls
from authenticate import urls as authenticate_urls
from django.views.generic import TemplateView



# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    # url(r'^docs/', include(swag_urls)),
    url(r'authenticate/',include(authenticate_urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# apiv1 = ApiSet(
#     urls=[
#         url(r'cust_dashboard/', include(dashboard_urls), name='person'),
# 	url(r'^docs/', include(swag_urls)),
# 	]
#     )

# urlpatterns = [
#     url(r'^api/v1/', include(apiv1,namespace='v1')),
#     url(r'^$', TemplateView.as_view(template_name='index.html')),
#     url(r'^map$', TemplateView.as_view(template_name='map.html')),
#     url(r'^admin/', admin.site.urls),
# ]

