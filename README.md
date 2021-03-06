# findp

Find and count letter 'p' (or other patterns) on Subreddits.

To use:

 - pip install -r requirements.txt
 - set the following environment vars: `SECRET_KEY`, `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`.
 - run manage.py migrations
 - run `manage.py count_p <subreddit> <pat> <limit>`

Example
    manage.py count_p learnpython p 10

RecordP
---

RecordP model is used to record pattern count and details for each run.
Example RecordP records after a few runs:

In [8]: from findp.models import RecordP

In [9]: l=RecordP.objects.all()

In [10]: l
Out[10]: <QuerySet [<RecordP: learnpython pattern=p count=816>, <RecordP: learnpython pattern=h count=1476>, <RecordP: learnpython pattern=how count=43>, <RecordP: learnpython pattern=can count=40>, <RecordP: learnpython pattern=what count=72>, <RecordP: learnpython pattern=what count=225>]>

Testing
---

To run tests:
 - run manage.py tests

Implementation Notes
---
Submission sorting order used is reddit's 'hot' sorting, but code could be changed (or an
argument added to management command class) to use other sorting methods listed in PRAW docs:
`https://praw.readthedocs.io/en/latest/getting_started/quick_start.html`
