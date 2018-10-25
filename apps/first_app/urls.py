from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.renderHome),
url(r'^dates$', views.renderDates),
url(r'^shop$', views.renderShop),
url(r'^music$', views.renderMusic),
url(r'^processEmail$', views.processEmail),
url(r'^processEmail_shop$', views.processEmail_shop)
]