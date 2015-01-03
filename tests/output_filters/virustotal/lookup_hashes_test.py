# -*- coding: utf-8 -*-
import testify as T
from osxcollector.output_filters.virustotal. \
    lookup_hashes import LookupHashesFilter
from tests.output_filters.run_filter_test import run_filter_test


class LookupHashesFilterTest(T.TestCase):

    def test_no_domains(self):
        input_blobs = [
            {'fungo': 'dingo', 'bingo': [11, 37], 'banana': {'a': 11}},
            {'span': 'div', 'head': ['tail', 22], 'orange': {'lemmon': 'zits'}}
        ]
        run_filter_test(lambda: LookupHashesFilter(), input_blobs, expected_output_blobs=input_blobs)
