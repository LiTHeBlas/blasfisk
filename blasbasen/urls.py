from django.conf.urls import patterns, include, url
from blasbasen.views import PersonList, PersonDetail, PersonAdd, PersonChange

urlpatterns = patterns('',
    #url(r'^$', 'blasbasen.views.index'),
    url(r'^person/$', PersonList.as_view()),
    url(r'^person/add/$', PersonAdd.as_view(template_name_suffix='_add')),
    url(r'^person/(?P<pk>\d+)/$', PersonDetail.as_view()),
    url(r'^person/(?P<pk>\d+)/change/$', PersonChange.as_view(template_name_suffix='_change')),
    #url(r'^person/(?P<user>\d+)/edit/$', 'blasbasen.views.person_edit'),
    #url(r'^person/(?P<user>\d+)/delete/$', 'blasbasen.views.person_delete'),
    
    #url(r'section/$', 'blasbasen.views.section_list'),
    #url(r'section/(?P<section>)/$', 'blasbasen.views.section_detail'),
    
)