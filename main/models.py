from django.db import models
from datetime import datetime




class Positions(models.Model):
    position = models.CharField(max_length=50,default=None,blank=True)

    def __str__(self):
      return f"{self.position}"
    

    class Meta:
        verbose_name_plural = "Positions"
        ordering = ['position']
  
class Posts(models.Model):
    post = models.CharField(max_length=400,default=None,blank=True)

    def __str__(self):
      return f"{self.post}"
    

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['post']

class TeamTypes(models.Model):
    types = models.CharField(max_length=50,default=None,blank=True)

    def __str__(self):
      return f"{self.types}"
    

    class Meta:
        verbose_name_plural = "Team Types"
        ordering = ['types']

class AgeGroups(models.Model):
    name = models.CharField(max_length=50,default=None,blank=True)

    def __str__(self):
      return f"{self.name}"
    

    class Meta:
        verbose_name_plural = "agegroups"
        ordering = ['name']

class Teams(models.Model):
    name = models.CharField(max_length=255,default=None, blank=True)
    description = models.CharField(max_length=500,default='Description here', blank=True, null=True)
    city = models.CharField(max_length=50,blank=True,null=True,default="")
    state = models.CharField(max_length=2,blank=True,null=True,default="")
    contactName = models.CharField(max_length=50,blank=True,null=True,default="")
    contactEmail = models.CharField(max_length=50,blank=True,null=True,default="")
    contactPhone = models.CharField(max_length=50,blank=True,null=True,default="")
    website = models.CharField(max_length=100,blank=True,null=True,default="")
    picture = models.ImageField(default='images/teams/default.png', upload_to='images/teams')
    instagramUser = models.CharField(max_length=255,default="instagram.com", blank=True)
    xUser = models.CharField(max_length=255,default="x.com", blank=True)
    slug = models.SlugField(default="", blank=True)
    posts = models.ManyToManyField(Posts, blank=True)
    teamTypes = models.ManyToManyField(TeamTypes, blank=True)
    agegroups = models.ManyToManyField(AgeGroups, blank=True)
    lookingforplayers = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    dateAdded = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Teams"
        ordering = ['name']


