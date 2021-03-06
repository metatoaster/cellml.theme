import os.path

import zope.interface
from zope.component import queryAdapter
from zope.publisher import browser
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

import z3c.form.field
import z3c.form.form
from z3c.form.i18n import MessageFactory as _
from plone.z3cform import layout
from plone.z3cform.templates import ZopeTwoFormTemplateFactory

import cellml.theme.browser
from cellml.theme.interfaces import ILayoutSettings
from cellml.theme.browser.interfaces import ICellMLThemeLayoutWrapper

path = lambda p: os.path.join(os.path.dirname(cellml.theme.browser.__file__),
                              'templates', p)


class ThemeLayoutForm(z3c.form.form.EditForm):
    """The theme selection form.
    """

    fields = z3c.form.field.Fields(ILayoutSettings)
    # see below.
    render = ViewPageTemplateFile(path('cellml_layout_wrapper.pt'))

    def getContent(self):
        """
        Since the object we want to edit is the annotations, we override
        the default method so it returns the adapted object for the
        apply method in parent.
        """

        return queryAdapter(self.context, name='CellMLThemeSettings')

    def content(self):
        """
        The render method has been replaced by a wrapper template to
        include the additional links, thus we need a separate method
        that will return the results of the form to it to render this.
        """
        return super(ThemeLayoutForm, self).render()

ThemeLayoutFormView = layout.wrap_form(ThemeLayoutForm,
    label=u'Select CellML Theme')
