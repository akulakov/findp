from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import re
import praw

from findp.models import RecordP

class Command(BaseCommand):
    reddit_class = praw.Reddit
    help = 'Count number of "p" letters or other patterns in given reddit forum.'

    def add_arguments(self, parser):
        parser.add_argument('forum', nargs=1, type=str)
        parser.add_argument('pattern', nargs='?', type=str, default='p')
        parser.add_argument('limit', nargs=1, type=int, default=10)

    def handle(self, *args, **options):

        reddit = self.reddit_class(
                     client_id = settings.REDDIT_CLIENT_ID,
                     client_secret = settings.REDDIT_CLIENT_SECRET,
                     user_agent = 'macos:findp-test-app:v0.1 (by /u/rainy-day-week)',
                   )

        count = 0
        forum = options['forum'][0]
        pattern = options['pattern']
        limit = options['limit'][0]

        display = self.stdout.write
        display(self.style.SUCCESS("= = = limit = = =   %s\n" % limit))

        for submission in reddit.subreddit(forum).hot(limit=limit):
            display(self.style.SUCCESS(submission.title))
            submission.comments.replace_more(limit=None)
            n = len(re.findall(pattern, submission.selftext, re.IGNORECASE))
            for c in submission.comments.list():
                n += len(re.findall(pattern, c.body, re.IGNORECASE))

            count += n
            display(self.style.SUCCESS('n %s\n' % n))
        display(self.style.SUCCESS('count %s' % count))
        RecordP.objects.create(forum=forum, pattern=pattern, count=count, limit=limit)
