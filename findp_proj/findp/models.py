from django.db import models as m

class RecordP(m.Model):
    site_choices = (('reddit','Reddit'),)

    created = m.DateTimeField(auto_now=True)
    forum   = m.CharField(max_length=300)
    site    = m.CharField(max_length=200, choices=site_choices, default='reddit')
    pattern = m.CharField(max_length=100)
    count   = m.IntegerField()
    limit   = m.IntegerField()

    def __str__(self):
        return '{} pattern={} count={}' \
                .format(self.forum, self.pattern, self.count)
