from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory, ISource
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# The values could potentially be user configurable, but this feature
# will not be used in this template as they are specifically defined.
# 
# First value in this tuple is the user description, the second value 
# is a tuple describing the combination for columns in the order of 
# (left, right, both), or the layout that will achieve the intended 
# style described by the label.
values = (
    (u'Both columns equal width (220px).', 
        (u'layoutFourSlim', u'layoutFourSlim', u'layoutOne',),),
    (u'Slim left, wide right (140px, 300px)', 
        (u'layoutFourSlimmer', u'layoutFour', u'layoutFive',),),
    (u'Wide left, slim right (300px, 140px)', 
        (u'layoutFour', u'layoutFourSlimmer', u'layoutTwo',),),
)
default_value = values[0][1]


class LayoutVocab(SimpleVocabulary):

    def __init__(self, context):
        self.context = context
        terms = [SimpleTerm(i[1], title=i[0]) for i in values]
        super(LayoutVocab, self).__init__(terms)

def LayoutVocabFactory(context):
    return LayoutVocab(context)

alsoProvides(LayoutVocabFactory, IVocabularyFactory)
