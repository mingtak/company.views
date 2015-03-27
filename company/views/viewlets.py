from five import grok
from zope.interface import Interface
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalFooter, IAboveContentBody, IBelowContent, IHtmlHead
from plone.app.contenttypes.interfaces import IDocument, INewsItem, IEvent
from company.content.productpage import IProductPage

"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Contace_IportalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(Interface)
    template = ViewPageTemplateFile('viewlets_template/contact.pt')

    def render(self):
        return self.template()


class SocialNetwork_IportalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(Interface)
    template = ViewPageTemplateFile('viewlets_template/scoialnetwork.pt')

    def render(self):
        return self.template()


class FbMessage_IBelowContent_IDocument(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IDocument)
    template = ViewPageTemplateFile('viewlets_template/fbmessage.pt')

    def render(self):
        return self.template()


class FbMessage_IBelowContent_INewsItem(FbMessage_IBelowContent_IDocument):
    grok.context(INewsItem)


class FbMessage_IBelowContent_IEvent(FbMessage_IBelowContent_IDocument):
    grok.context(IEvent)


class FbMessage_IBelowContent_IProductPage(FbMessage_IBelowContent_IDocument):
    grok.context(IProductPage)


class Disqus_IBelowContent_INewsItem(FbMessage_IBelowContent_IDocument):
    grok.context(INewsItem)
    template = ViewPageTemplateFile('viewlets_template/disqus.pt')


class Disqus_IBelowContent_IDocument(Disqus_IBelowContent_INewsItem):
    grok.context(IDocument)


class Disqus_IBelowContent_IEvent(Disqus_IBelowContent_INewsItem):
    grok.context(IEvent)


class Disqus_IBelowContent_IProductPage(Disqus_IBelowContent_INewsItem):
    grok.context(IProductPage)


class Addthis_IAboveContentBody_INewsItem(grok.Viewlet):
    grok.viewletmanager(IAboveContentBody)
    grok.context(INewsItem)
    template = ViewPageTemplateFile('viewlets_template/addthis.pt')

    def render(self):
        return self.template()

class Addthis_IAboveContentBody_IDocument(Addthis_IAboveContentBody_INewsItem):
    grok.context(IDocument)


class Addthis_IAboveContentBody_IEvent(Addthis_IAboveContentBody_INewsItem):
    grok.context(IEvent)


class Addthis_IAboveContentBody_IProductPage(Addthis_IAboveContentBody_INewsItem):
    grok.context(IProductPage)


class WebAnalyticsCode_IPortalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(Interface)
    template = ViewPageTemplateFile('viewlets_template/webanalyticscode.pt')

    def render(self):
        return self.template()


class MetaCode_IHtmlHead_Interface(grok.Viewlet):
    grok.viewletmanager(IHtmlHead)
    grok.context(Interface)
    template = ViewPageTemplateFile('viewlets_template/metacode.pt')

    def render(self):
        return self.template()
