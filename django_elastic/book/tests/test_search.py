from django import test
from django.conf import settings
from elasticsearch import Elasticsearch

from haystack.query import SearchQuerySet


class SearchTest(test.TestCase):
    # def setUp(self):
    #     es = Elasticsearch(settings.HAYSTACK_CONNECTIONS['default']['URL'])
    #     es.indices.create(index='test-index', ignore=400)
    #
    # def tearDown(self):
    #     pass

    def test_search_all(self):
        all_results = SearchQuerySet().all()
        count = all_results.count()

    def test_search_book(self):
        all_results = SearchQuerySet().filter(content="Python")
        count = all_results.count()
