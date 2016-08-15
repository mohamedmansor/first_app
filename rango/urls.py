from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_id>\d+)/$',
        views.get_category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_page/$', views.add_page, name='add_page'),
    # url(r'^add_page/(?P<category_id>\d+)/$',
    #     views.add_page, name='add_page'),
    # url(r'^goto/$', views.track_url, name='goto'),


]
