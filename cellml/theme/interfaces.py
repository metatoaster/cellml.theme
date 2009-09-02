import zope.interface
import zope.schema
from plone.portlets.interfaces import IPortletManager


class ILayoutSettings(zope.interface.Interface):
    """\
    Maps between the two thing,
    """

    layout = zope.schema.Choice(
        title=u'Layout Choice',
        description=u"The layout style to use with this page; 'no value' indicates automatic.",
        vocabulary='LayoutVocab',
        required=False,
    )

    def get_layout(sl, sr):
        """\
        Return the layout based on the columns.
        """


class ICellMLHeaderPortlets(IPortletManager):
    """\
    CellML Header portlets - can be used for sponsor messages.
    """


class ICellMLFooterPortlets(IPortletManager):
    """\
    CellML Footer portlets, this goes below all content, but above the 
    sticky footer.
    """


class ICellMLStickyFooterPortlets(IPortletManager):
    """\
    CellML Sticky footer portlets, for content that sticks to the bottom
    of pages.
    """
