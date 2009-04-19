import zope.interface
import zope.schema

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
