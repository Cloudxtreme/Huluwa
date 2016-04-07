from django.conf.urls import url
from SmartPXE import views
urlpatterns = [
    url(r'^client-list$', views.get_client_list, name="client_list"),
    url(r'^os-list$', views.get_os_list, name="os_list"),
]
