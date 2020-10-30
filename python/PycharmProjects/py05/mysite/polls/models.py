from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length= 200, unique=True)
    pub_date = models.DateField()
    def __str__(self):
        return ('Q: %s' % self.question_text)

class Choice(models.Model):
    choice_text = models.CharField (max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)
    def __str__(self):
        return ('%s :----->%s' % (self.question,self.choice_text) )


