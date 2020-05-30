from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

staff = User.objects.filter(is_staff=True)
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
    agent_att = models.ForeignKey(User,on_delete = models.CASCADE,related_name="Mifga.author+",default = "1")
    comment = models.TextField(default='')
    subscribed_to_issue = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('my-issues')

    def __str__(self):
        return self.title


