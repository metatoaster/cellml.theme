from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from plone.app.layout.viewlets.common import PersonalBarViewlet
from plone.app.layout.viewlets.common import PathBarViewlet

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the vielwet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

#class MyViewlet(ViewletBase):
#    render = ViewPageTemplateFile('viewlet.pt')
#
#    def update(self):
#        self.computed_value = 'any output'


class CellMLLogoViewlet(ViewletBase):
    index = ViewPageTemplateFile('cellml_logo.pt')

    def update(self):
        super(CellMLLogoViewlet, self).update()

        self.navigation_root_url = self.portal_state.navigation_root_url()

        portal = self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()

        self.portal_title = self.portal_state.portal_title()


class CellMLSearchBoxViewlet(ViewletBase):
    """\
    Can customize this to search through many different things.
    """

    index = ViewPageTemplateFile('searchbox.pt')

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
    index = ViewPageTemplateFile('sections.pt')


class CellMLPersonalBarViewlet(PersonalBarViewlet):
    pass

class CellMLPathBarViewlet(PathBarViewlet):
    pass
