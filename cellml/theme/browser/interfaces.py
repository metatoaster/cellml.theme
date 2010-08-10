from zope.viewlet.interfaces import IViewletManager
from plone.theme.interfaces import IDefaultPloneLayer
from plone.z3cform.interfaces import IFormWrapper


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "CellML Theme" theme, this interface must be its layer
       (in theme/viewlets/configure.zcml).
    """


class ICellMLStickyFooter(IViewletManager):
    """Viewlet manager for the sticky footers."""


class ICellMLThemeLayoutWrapper(IFormWrapper):
    """Layout wrapper for CellML Theme."""
