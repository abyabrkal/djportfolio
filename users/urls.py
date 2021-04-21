from django.conf.urls import include, url
from . import views


urlpatterns = [
    url('', views.dashboard, name="dashboard"),
    url('accounts/', include('django.contrib.auth.urls')),
]


