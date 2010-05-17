from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.viewlets.common import PersonalBarViewlet
from plone.app.layout.viewlets.common import PathBarViewlet


class CellMLLogoViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/cellml_logo.pt')

    def update(self):
        super(CellMLLogoViewlet, self).update()

        self.navigation_root_url = self.portal_state.navigation_root_url()

        portal = self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()

        self.portal_title = self.portal_state.portal_title()


class CellMLLogoLinkedViewlet(CellMLLogoViewlet):

    def update(self):
        super(CellMLLogoLinkedViewlet, self).update()
        self.protocol = 'http'
        # XXX cellml.org still needs https.
        #self.protocol = self.navigation_root_url.split('://')[0]
        # <3 CellML.
        self.navigation_root_url = '%s://www.cellml.org/' % self.protocol


class CellMLSearchBoxViewlet(ViewletBase):
    """\
    Can customize this to search through many different things.
    """

    index = ViewPageTemplateFile('templates/searchbox.pt')

    def update(self):
        super(CellMLSearchBoxViewlet, self).update()

        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')

        props = getToolByName(self.context, 'portal_properties')
        livesearch = props.site_properties.getProperty('enable_livesearch', False)
        if livesearch:
            self.search_input_id = "searchGadget"
        else:
            self.search_input_id = ""

        folder = context_state.folder()
        self.folder_path = '/'.join(folder.getPhysicalPath())


class CellMLGlobalSectionsViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile('templates/sections.pt')


class CellMLPersonalBarViewlet(PersonalBarViewlet):
    pass


class CellMLPathBarViewlet(PathBarViewlet):
    pass


class CellMLPartOfIUPSViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/iups_logo.pt')


class CellMLPartOfFillerViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/filler.pt')


class PhysiomeLogoLinkedViewlet(CellMLLogoViewlet):
    index = ViewPageTemplateFile('templates/physiome_logo.pt')

    def update(self):
        super(PhysiomeLogoLinkedViewlet, self).update()
        self.protocol = 'http'
        # XXX physiomeproject.org still needs https.
        #self.protocol = self.navigation_root_url.split('://')[0]
        self.navigation_root_url = '%s://physiomeproject.org/' % self.protocol
