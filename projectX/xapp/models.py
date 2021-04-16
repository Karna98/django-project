from django.db import models

# Create your models here.

# Table with "Topic" name will be created
class Topics(models.Model):
    # Title of the Topic
    # { Data Type = Characters, Max Length = 200 }
    topic_title = models.CharField(max_length=200)
    # Date at which topic was created
    # { Data Type = DateTime }
    published_date = models.DateTimeField('date published')

# Table with "Opinions" name will be created
class Opinions(models.Model):
    # Referencing to ID of Topic bydefault created as primary key in 'Topics' table
    # { Foreign Key, 'on_delete=models.CASCADE' - will be deleted when topic_id is deleted from 'Topics' table}
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    # Opinion for the topic
    # { Data Type = Characters, Max Length = 200 }
    opinion = models.CharField(max_length=200)
    # No. of Votes
    # { Data Type = Integer, Default Valur = 0 }
    votes = models.IntegerField(default=0)
