from django.db import models

# Create your models here.
class Job(models.Model):
	job_title =  models.CharField(max_length = 100)
	job_des = models.TextField()
	job_sal = models.IntegerField()
	job_loc = models.CharField(max_length = 50)

	def __str__(self):
		return self.job_title

class Contact(models.Model):
	name=models.CharField(max_length=100)
	mail=models.EmailField()
	contactNumber=models.IntegerField()
	message=models.TextField()

	def __str__(self):
		return self.name

class Enquiry(models.Model):
	name=models.CharField(max_length=100)
	contactNumber=models.IntegerField()
	company=models.CharField(max_length=100)
	post=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	description=models.TextField()

	def __str__(self):
		return self.company

class Partner(models.Model):
	PLACEMENT_AGENCY='PAS'
	FREELANCER='FLS'
	NGO='NGO'
	TRAINING_INSTITUTE='TIS'
	CYBER_CAFE='CCS'
	COLLEGE='CLG'
	TYPES=[
		(PLACEMENT_AGENCY,'PlacementAgency'),
		(FREELANCER,'Freelancer'),
		(NGO,'Ngo'),
		(TRAINING_INSTITUTE,'TrainingInstitute'),
		(CYBER_CAFE,'CyberCafe'),
		(COLLEGE,'College')
	]
	organisationType=models.CharField(max_length=3,choices=TYPES,default="PLACEMENT_AGENCY")
	organisationName=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	email=models.EmailField()
	contactNumber=models.IntegerField()
	experience=models.IntegerField()

	def __str__(self):
		return self.organisationName
