from zope import interface
from zope.component import queryAdapter, queryMultiAdapter
from zope.publisher import browser
from zope.contentprovider.interfaces import IContentProvider

from Acquisition import Explicit
from Products.CMFPlone.browser.interfaces import IPlone


class Layout(Explicit):
    """Snippet to render the header div for the layout
    """

    interface.implements(IContentProvider)

    def __init__(self, context, request, view):
        self.__parent__ = view
        self.view = view
        self.context = context
        self.request = request

    def update(self):
        pass

    def render(self):
        """
        This method returns the name of the template the particular view
        should use, based on which columns are populated with portlets
        and whether a specific theme layout was chosen for the context.
        """

        # Since ploneview.Plone has support for older global_defines but
        # implemented in a way that we don't want to replicate here (as
        # legacy Plone code can be quite ugly), we try to see if we can
        # use it by checking whether the view we have is one such thing.
        # 
        # When Plone removes support for legacy option check or if we
        # decide this is unnecessary, remove this section.
        use_default = IPlone.providedBy(self.view)

        if use_default:
            # since we are accessing private members...
            try:
                sl = self.view._data['sl']
                sr = self.view._data['sr']
            except:
                # it may fail...
                use_default = False

        if not use_default:
            # this is the correct way, will be done if the above cannot
            # be done.
            ploneview = queryMultiAdapter((self.context, self.request), 
                                          name='plone')
            sl = ploneview.have_portlets('plone.leftcolumn', self.view)
            sr = ploneview.have_portlets('plone.rightcolumn', self.view)

        # This allows override of template via self.request for whatever 
        # reason.  Might be necessary to allow "merging" of this using
        # another variable?
        if self.request.other.get('sl') is not None:
            sl = bool(self.request.other.get('sl'))
        if self.request.other.get('sr') is not None:
            sr = bool(self.request.other.get('sr'))

        o = queryAdapter(self.context, name='CellMLThemeSettings')
        self.layout = o.get_layout(sl, sr)

        return self.layout
