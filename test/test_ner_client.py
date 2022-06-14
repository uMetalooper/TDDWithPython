from cmath import exp
import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble, NerDisplacyTestDouble

class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])

        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])

        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'LQL', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        
        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'LQL','label':'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'abc', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)

        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'abc','label':'Group'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])
    
    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'abc', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)

        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'abc','label':'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'abc', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'abc','label':'Language'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'abc', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)

        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'abc','label':'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'abc', 'label_': 'GPE'}, {'text':'LQL','label_':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'ents':[{'ent':'abc','label':'Location'}, {'ent':'LQL','label':'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_html_from_model(self):
        # mock for named entity model
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        
        # mock for displacy
        displacy = NerDisplacyTestDouble('')
        displacy.returns_html('<h2><h2>')

        ner = NamedEntityClient(model, displacy)
        result = ner.get_ents('...')
        expected_result = {'html': '<h2><h2>'}
        self.assertEqual(result['html'], expected_result['html'])