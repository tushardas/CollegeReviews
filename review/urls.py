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
    url(r'^collreview',views.view_review,name='collreview'),
    url(r'^addcoll',views.add_coll,name='addcoll'),
    url(r'^addreview',views.add_review,name='addreview'),
    url(r'^signup',views.register,name='signup'),
    url(r'^login',views.login,name='login'),
    url(r'^requestlogin',views.reqlogin,name='reqlogin'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^list',views.list,name='list'),
    #url(r'^about',views.about,name='about')
)
