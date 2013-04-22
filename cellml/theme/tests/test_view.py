from unittest import TestSuite, makeSuite

from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

from cellml.theme.tests.base import TestCase


class ViewTestCase(TestCase):

    def test_base(self):
        view = self.portal.restrictedTraverse('front-page/@@cellml_theme')
        self.assertEqual(view.columns(), ('span12', 'span0', 'span0'))

    def test_news(self):
        self.setRoles(['Manager', 'Reviewer'])
        self.portal.news.invokeFactory('News Item', id='item')
        self.portal.news.item.edit(text='bar', text_format='html', title='Foo')
        view = self.portal.restrictedTraverse('news/item/@@cellml_theme')
        self.assertEqual(view.columns(), ('span9', 'span3', 'span0'))

        self.portal.portal_workflow.doActionFor(
            self.portal.news.item, 'publish')
        view = self.portal.restrictedTraverse('news/aggregator/@@cellml_theme')
        self.assertEqual(view.columns(), ('span6', 'span3', 'span3'))

        view = self.portal.restrictedTraverse('front-page/@@cellml_theme')
        self.assertEqual(view.columns(), ('span9', 'span0', 'span3'))

    def test_manage_portlets(self):
        self.setRoles(['Manager', 'Reviewer'])
        view = self.portal.restrictedTraverse('front-page/@@manage-portlets')
        # XXX as the manage-portlets does not give any easy-to-access
        # hints for notifying the need for columns, we can't do anything
        # here.
        self.assertEqual(view.columns(), ('span12', 'span0', 'span0'))


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(ViewTestCase))
    return suite
