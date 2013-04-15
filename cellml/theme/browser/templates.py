from os.path import join
from os.path import dirname

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

root = dirname(__file__)
path = lambda x: join(root, 'templates', x)
