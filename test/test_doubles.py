class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

class SpanTestDouble:
    """
    Test double for spaCy Span
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label

class NerDisplacyTestDouble:
    """
    Test double for spaCy Displacy
    """
    def __init__(self, displacy):
        self.displacy = displacy

    def returns_html(self, html):
        self.html = html

    def render(self, listOfDocs, style):
        return self.html