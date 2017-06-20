from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"The project is {self.name}"

    class Meta:
        ordering = ['name']


class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.name
