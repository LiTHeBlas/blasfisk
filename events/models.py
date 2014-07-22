# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group

answers = (
    ('No', 'Nej'),
    ('Maybe', 'Kanske'), # TODO: Ska vi ha ett sånt här alternativ?
    ('Yes', 'Ja'),
)

class EventType(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
class Attendance(models.Model):
    #Skapas när användaren bjuds in till eller själv går med i ett evenemang
    event = models.ForeignKey('Event')
    person = models.ForeignKey('blasbase.Person')
    
    answer = models.CharField(max_length=8, choices=answers, blank=True) # Blank = inget svar

class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    type = models.ForeignKey(EventType)
    public = models.BooleanField()
    attendees = models.ManyToManyField('blasbase.Person', through=Attendance)
    
    customer = models.ForeignKey('blasbase.Customer')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class TargetedInfo(models.Model):
    event = models.ForeignKey(Event)
    group = models.ForeignKey(Group)
    content = models.TextField()