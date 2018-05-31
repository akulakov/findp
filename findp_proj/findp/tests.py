from django.test import TestCase
from django.core.management import call_command
from unittest.mock import MagicMock, patch

from findp.models import RecordP

class TestCountP(TestCase):
    @patch('findp.management.commands.count_p.Command.reddit_class')
    def test_count_p(self, MockClass):
        "Test count_p command."
        # import findp
        # findp.management.commands.count_p.Command.praw_class = MagicMock
        args = ['learnpython', 'how', 10]
        call_command('count_p', *args)
        rec = RecordP.objects.first()
        self.assertEquals(rec.forum, 'learnpython')
        self.assertEquals(rec.pattern, 'how')
        self.assertEquals(rec.limit, 10)
