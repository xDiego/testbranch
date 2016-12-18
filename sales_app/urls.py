from django.conf.urls import url
import views

urlpatterns = [
    url('^$', views.home_page, name='home_page'),
    url('^form/$', views.handle_form, name='handle_form'),
]
