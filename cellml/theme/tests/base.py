from Testing import ZopeTestCase as ztc
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup


@onsetup
def setup():
    fiveconfigure.debug_mode = True
    import cellml.theme
    zcml.load_config('configure.zcml', cellml.theme)
    fiveconfigure.debug_mode = False
    ztc.installPackage('cellml.theme')

setup()
ptc.setupPloneSite(extension_profiles=(
    'cellml.theme:default',
))

class TestCase(ptc.PloneTestCase):
    """
    Base test class.
    """
