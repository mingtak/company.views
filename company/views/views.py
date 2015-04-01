from five import grok
from zope.interface import Interface
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.interfaces import IDocument, INewsItem, IEvent
from plone.app.multilingual.interfaces import ILanguage
from company.content.productpage import IProductPage


grok.templatedir('views_template')

class PrivatePage(grok.View):
    grok.context(Interface)
    grok.name('private_page')
    grok.template('private_page')

    def update(self):
        return


class SearchPage(grok.View):
    grok.context(Interface)
    grok.name('searchpage')
    grok.template('searchpage')

    def update(self):
        context = self.context
        request = self.request
        catalog = context.portal_catalog
        language = ILanguage(context).get_language()
        SearchableText = getattr(request, 'SearchableText', '').strip()
        if SearchableText == '':
            self.brain = []
            return
        self.brain = catalog({'SearchableText':SearchableText,
                              'Language':language,
                              'Type':['Document', 'Event', 'News Item', 'ProductPage']},
                             sort_on='modified',
                             sort_order='reverse')
        if len(self.brain) == 0:
            self.brain = []
        return
