from zope import interface
from zope.component import queryAdapter, queryMultiAdapter
from zope.publisher import browser
from zope.contentprovider.interfaces import IContentProvider

from Acquisition import aq_inner, aq_parent, Explicit
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

    def _ploneview_slots(self):
        # Since ploneview.Plone has support for older global_defines but
        # implemented in a way that we don't want to replicate here (as
        # legacy Plone code can be quite ugly), we try to see if we can
        # use it by checking whether the view we have is one such thing.
        # 
        # When Plone removes support for legacy option check or if we
        # decide that check is unnecessary, remove this method.
        if IPlone.providedBy(self.view):
            # since we are accessing private members...
            try:
                sl = self.view._data['sl']
                sr = self.view._data['sr']
                return sl, sr
            except:
                # it may fail...
                pass
        return None

    def slot_status(self):
        ploneview = queryMultiAdapter((self.context, self.request), 
                                      name='plone')
        sl = ploneview.have_portlets('plone.leftcolumn', self.view)
        sr = ploneview.have_portlets('plone.rightcolumn', self.view)
        return sl, sr

    def slot_overrides(self, sl, sr):
        # This allows override of template via self.request for whatever 
        # reason.  Might be necessary to allow "merging" of this using
        # another variable?
        if self.request.other.get('sl') is not None:
            sl = bool(self.request.other.get('sl'))
        if self.request.other.get('sr') is not None:
            sr = bool(self.request.other.get('sr'))
        return sl, sr

    def get_slots(self):
        d = self._ploneview_slots()
        if d:
            sl, sr = d
        else:
            sl, sr = self.slot_status()
        sl, sr = self.slot_overrides(sl, sr)
        return sl, sr

    def render(self):
        """
        This method returns the name of the template the particular view
        should use, based on which columns are populated with portlets
        and whether a specific theme layout was chosen for the context.
        """

        sl, sr = self.get_slots()
        context = aq_inner(self.context)
        o = None
        while context is not None:
            # see if parents have a specific layout set.
            try:
                o = queryAdapter(context, name='CellMLThemeSettings')
                if o.layout is not None:
                    # we have layout, we are done.
                    break
            except:
                pass
            context = aq_parent(context)

        if not o:
            # We cannot find the answer.
            return None

        self.layout = o.get_layout(sl, sr)
        return self.layout
