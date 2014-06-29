# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.admin import StackedInline
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from blasstrap.models import Carousel, CarouselEntry, Jumbotron, Pusher, PusherEntry
from django.utils.translation import ugettext_lazy as _


class JumbotronPlugin(CMSPluginBase):
    name = _(u'Jumbotron')
    module = _(u'Bootstrap')

    model = Jumbotron
    render_template = "plugins/jumbotron.html"
    allow_children = True
    child_classes = ['TextPlugin']


class CarouselEntryInline(StackedInline):
    model = CarouselEntry
    extra = 3


class CarouselPlugin(CMSPluginBase):
    name = _(u'Carousel')
    module = _(u'Bootstrap')

    model = Carousel
    allow_children = False
    render_template = "plugins/carousel.html"

    inlines = [CarouselEntryInline]


class PusherEntryInline(StackedInline):
    model = PusherEntry
    extra = 3


class PusherPlugin(CMSPluginBase):
    name = _(u'Pusher')
    module = _(u'Bootstrap')

    model = Pusher
    allow_children = False
    render_template = "plugins/pusher.html"

    inlines = [PusherEntryInline]

plugin_pool.register_plugin(JumbotronPlugin)
plugin_pool.register_plugin(CarouselPlugin)
plugin_pool.register_plugin(PusherPlugin)

settings.CMS_PLACEHOLDER_CONF['jumbotron-content'] = {
    'name': _(u'Jumbotron content'),
    'default_plugins': [
        {
            'plugin_type': 'TextPlugin',
            'values': {
                'body': u"""
                    <h1>Jumbotron</h1><p>Innehållet i en jumbotron kan bestå av det mesta, men håll dig till
                    vanliga <code>h1</code> osv. samt <code>p</code> i textväg.</p>
                """
            },
        },
    ]
}

settings.CMS_PLACEHOLDER_CONF['pusher-content'] = {
    'name': _(u'Jumbotron content'),
    'default_plugins': [
        {
            'plugin_type': 'TextPlugin',
            'values': {
                'body': u"""
                    <p>&nbsp;&nbsp;&nbsp;</p>
                """
            },
        },
    ]
}