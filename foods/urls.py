from django.conf.urls import url
from django.contrib import admin
from . import views

app_name="foods"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name="index"),
    url(r'^create/$', views.create_receipe, name="create"),
    url(r'^details/(?P<receipe_id>[0-9]+)/$', views.details, name="details"),
    url(r'^delete/(?P<receipe_id>[0-9]+)/$', views.delete, name="delete"),
    url(r'^registration/$', views.registration, name="registration"),
    url(r'^login_view/$', views.login_view, name="login_view"),
    url(r'^logout_view/$', views.logout_view, name="logout_view"),
    url(r'^createform/$', views.createform, name="createform"),

]
