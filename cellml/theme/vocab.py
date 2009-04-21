from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory, ISource
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# The values could potentially be user configurable, but this feature
# will not be used in this template as they are specifically defined.
# First value is the key, second value is the description.
values = (
    (1, u'Both columns equal width (220px)'),
    (2, u'Slim left, wide right (140px, 300px)'), 
    (3, u'Wide left, slim right (300px, 140px)'), 
)

# The index would be a dict with key from the first element of the 
# values from above, and the value will be a tuple for the styles to
# be applied if there are only left, right or both columns visible in
# the view.
index = {
    1: (u'layoutFourSlim', u'layoutFourSlim', u'layoutOne',),
    2: (u'layoutFourSlimmer', u'layoutFour', u'layoutFive',),
    3: (u'layoutFour', u'layoutFourSlimmer', u'layoutTwo',),
}
default_value = index[1]

def get_layout(i):
    # XXX this method should probably belong in a util method, along
    # with values above.
    return index.get(i, default_value)


class LayoutVocab(SimpleVocabulary):

    def __init__(self, context):
        self.context = context
        terms = [SimpleTerm(i[0], title=i[1]) for i in values]
        super(LayoutVocab, self).__init__(terms)

    def getTerm(self, value):
        """\
        An upgrade or change to the values above may break this, so we
        need to allow all terms.
        """

        try:
            return super(LayoutVocab, self).getTerm(value)
        except LookupError:
            return SimpleTerm(value)

def LayoutVocabFactory(context):
    return LayoutVocab(context)

alsoProvides(LayoutVocabFactory, IVocabularyFactory)
