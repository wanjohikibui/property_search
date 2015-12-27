from django.conf.urls import patterns, include, url
from django.contrib import admin
from search.views import * 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from search.models import *
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth import views
from django.contrib.auth import urls


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='portal/index.html'), name='index'),
    url(r'^accounts/login/$', 'search.views.user_login', name='login'),
    url(r'^accounts/logout/', 'search.views.user_logout', name='loggedout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),     
    url(r'^register/$', 'search.views.register_user', name='register_user'),
    url(r'^confirm/(?P<activation_key>\w+)/', ('search.views.register_confirm')), 
    url(r'^contacts/$','search.views.contact', name='contacts'),  
    url(r'^apply/$', 'search.views.application_portal', name='apply'), 
    url(r'^status/$', 'search.views.status', name='status'),
    url(r'^map/$', 'search.views.map', name='map'),
    url(r'^parcel_data/$', GeoJSONLayerView.as_view(model=parcel, properties=('objectid','lr_number','shape_leng','shape_area')), name='data'),
    url(r'^search/', searchIndex.as_view(), name="search"),
    url(r'^parcel/(?P<slug>\S+)$', parcelDetail.as_view(), name="parcel_detail"),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^password/$', 'django.contrib.auth.views.password_reset', {}, 'password_reset'),
    url(r'^accounts/password_change/$','django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/'}, 
        name="password_change"), 
    url(r'^accounts/password_change/done/$','django.contrib.auth.views.password_change_done'),
    url(r'^accounts/password_reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    url(r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    url(r'^accounts/password_reset/complete/$', 
        'django.contrib.auth.views.password_reset_complete') 
					    
)