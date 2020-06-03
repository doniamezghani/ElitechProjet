from __future__ import unicode_literals

from django.db import models
class Course(models.Model):
	name = models.CharField(max_length=20 , default='')
	content = models.TextField()
	duration = models.CharField(max_length=20, default='')
	video = models.FileField(upload_to='upload/' , default='')
	image = models.ImageField(upload_to='upload/' , default='')
	price = models.CharField(max_length=20, default='')
	total_students = models.CharField(max_length=20, default='' )
	def __str__(self):
		return self.name

class Chapitre(models.Model):
	name = models.CharField(max_length=20)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
class Quiz(models.Model):
	name = models.CharField(max_length=20)
	chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
class Question(models.Model):
    name = models.CharField(max_length=20)
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.name