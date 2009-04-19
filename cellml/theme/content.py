from zope import interface
from zope import component
from zope.schema import fieldproperty
from zope.annotation import factory
from zope.annotation.attribute import AttributeAnnotations
from persistent import Persistent

from cellml.theme.interfaces import ILayoutSettings
from cellml.theme.vocab import default_value


class LayoutSettings(Persistent):
    """\
    Maps between the two thing,
    """

    interface.implements(ILayoutSettings)
    component.adapts(interface.Interface)

    layout = fieldproperty.FieldProperty(ILayoutSettings['layout'])

    def get_layout(self, sl, sr):
        """\
        Returns the new URI to the model, given the old model name.
        """

        try:
            leftcolumn, rightcolumn, bothcolumns = self.layout
        except:
            leftcolumn, rightcolumn, bothcolumns = default_value

        # a simple truth table to figure this out.
        return {
            (False, False): u'layoutZero',
            (True, False): leftcolumn,
            (False, True): rightcolumn,
            (True, True): bothcolumns,
        }[(sl, sr)]


LayoutSettingsFactory = factory(LayoutSettings)
