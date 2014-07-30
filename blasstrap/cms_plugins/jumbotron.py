# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from blasstrap.models import Jumbotron

class JumbotronPlugin(CMSPluginBase):
    name = _(u'Jumbotron')
    module = _(u'Bootstrap')

    model = Jumbotron
    render_template = "plugins/jumbotron.html"
    allow_children = True
    child_classes = ['TextPlugin']

plugin_pool.register_plugin(JumbotronPlugin)

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