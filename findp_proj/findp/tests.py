from django.test import TestCase
from django.core.management import call_command
from unittest.mock import MagicMock, Mock, patch

from findp.models import RecordP

class TestCountP(TestCase):
    def test_count_p(self):
        "Test count_p command."
        with patch('findp.management.commands.count_p.Command.reddit_class') as reddit_mock:
            subm_mock = MagicMock()
            subm_mock.selftext = 'hello how how hi hi how'
            reddit_mock.return_value.subreddit.return_value.hot.return_value = [subm_mock]
            args = ['learnpython', 'how', 10]
            call_command('count_p', *args)
            rec = RecordP.objects.first()
            self.assertEquals(rec.forum, 'learnpython')
            self.assertEquals(rec.pattern, 'how')
            self.assertEquals(rec.limit, 10)
            self.assertEquals(rec.count, 3)
