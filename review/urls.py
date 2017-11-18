from django.conf.urls import patterns, include, url
from review import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango.views.home', name='home'),
    # url(r'^tango/', include('tango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^login',views.login,name='login'),
    #url(r'^about',views.about,name='about')
)
