from zope.component import queryAdapter
from zope.publisher import browser
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

import z3c.form.field
import z3c.form.form
from z3c.form.i18n import MessageFactory as _
from plone.z3cform import layout

from cellml.theme.interfaces import ILayoutSettings


class ThemeLayoutForm(z3c.form.form.EditForm):
    """The theme selection form.
    """

    fields = z3c.form.field.Fields(ILayoutSettings)

    def getContent(self):
        """
        Since the object we want to edit is the annotations, we override
        the default method so it returns the adapted object for the
        apply method in parent.
        """

        return queryAdapter(self.context, name='CellMLThemeSettings')

ThemeLayoutFormView = layout.wrap_form(ThemeLayoutForm, 
    label=u'Select CellML Theme')
