from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^home/', views.home, name = "home"),
    url(r'^shop/', views.shop, name="shop"),
    url(r'^naturalhairblog/', views.blog, name = 'blog'),
    url(r'^contact/', views.contact, name = 'contact'),
    url(r'^posts/', views.post, name = 'post'),
    url(r'^reviews', views.reviews, name = 'reviews'),
    url(r'^services', views.services, name = 'services'),
    url(r'^registration', views.UserFormView.as_view(), name = 'registration'),
    url(r'^login', views.LoginFormView.as_view(), name = 'login'),
    url(r'^userpage', views.userpage, name = 'userpage'),
]

