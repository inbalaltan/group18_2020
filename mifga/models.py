from django.db import models
from django.contrib.auth.models import User
status_choices = (
    ('open','OPEN'),('in progress','IN PROGRESS'),('closed','CLOSED'),
)
obs_choices = (
    ('מקלטים','מקלטים'),('נקיון','נקיון'),('פארקים','פארקים'),('רמזורים','רמזורים'),
    ('כבישים ומדרכות','כבישים ומדרכות'),('מוסדות חינוך','מוסדות חינוך'),('מים','מים'),('מצלמות','מצלמות'),
    ('בעלי חיים','בעלי חיים'),('גינון','גינון'),('חניה','חניה'),('חשמל ותאורה','חשמל ותאורה'),
    ('ביוב','ביוב'),('אחר','אחר'),
)
class Mifga(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    street = models.CharField(max_length=15)
    house_number = models.CharField(max_length=3)
    letter = models.CharField(max_length=1, default='0')
    neighborhood = models.CharField(max_length=25, default='0')
    status = models.CharField(max_length = 255,choices=status_choices, default='open')
    obs_title = models.CharField(max_length = 255,choices=obs_choices, default='אחר')
    comment = models.TextField(default='None')

    def __str__(self):
        return self.title


