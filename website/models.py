from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

	class Meta:
		abstract = True # Set this model as Abstract

class Message(TimeStampedModel):
	name = models.CharField(max_length=25, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	message = models.TextField(max_length=850, blank=True, null=True)

	def __str__(self):
		return str(self.name)

class Home(TimeStampedModel):
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(max_length=600, null=True, blank=True)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return str(self.title)

class Language(TimeStampedModel):
	name = models.CharField(max_length=100)
	lang_code = models.CharField(max_length=20)
	default = models.BooleanField(default=False)
	order = models.IntegerField(blank=True)

	def __str__(self):
		return str(self.name)

class Social(TimeStampedModel):
	owner = models.CharField(max_length=100, blank=True, null=True)
	facebook = models.URLField(max_length=100, blank=True, null=True)
	twitter = models.URLField(max_length=100, blank=True, null=True)
	youtube = models.URLField(max_length=100, blank=True, null=True)
	linkedin = models.URLField(max_length=100, blank=True, null=True)
	scopus = models.URLField(max_length=100, blank=True, null=True)
	research_gate = models.URLField(max_length=100, blank=True, null=True)
	github = models.URLField(max_length=100, blank=True, null=True)
	other_link1 = models.URLField(max_length=100, blank=True, null=True)
	other_link2 = models.URLField(max_length=100, blank=True, null=True)

	def __str__(self):
		return str(self.owner)


class LabDetails(TimeStampedModel):
	name = models.CharField(max_length=100, blank=True)
	description = RichTextField(max_length=10000, blank=True)
	email = models.EmailField(max_length=100, blank=True)
	social = models.ForeignKey(Social, blank=True, null=True)
	address = models.CharField(max_length=150, blank=True, null=True)
	phone = models.CharField(max_length=150, blank=True, null=True)
	mobile = models.CharField(max_length=150, blank=True, null=True)
	logo = models.ImageField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	fax = models.CharField(max_length=150, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Lab Details"

	def __str__(self):
		return str(self.name)

class Person(TimeStampedModel):
	FACULTY_CHOICES = (
				("Head of Translog", "Head of Translog"),
				("Senior Research Fellows", "Senior Research Fellows"),
				("Research Fellows", "Research Fellows"),
				("Visiting Research Fellows", "Visiting Research Fellows"),
				("PhD Students", "PhD Students"),
			)

	FACULTY_CHOICES_GR = (
				("Υπεύθυνος Εργαστηρίου", "Υπεύθυνος Εργαστηρίου"),
				("Πρεσβύτεροι Ερευνητές", "Πρεσβύτεροι Ερευνητές"),
				("Ερευνητές", "Ερευνητές"),
				("Επισκέπτες Ερευνητές", "Επισκέπτες Ερευνητές"),
				("Μεταπτυχιακοί Φοιτητές", "Μεταπτυχιακοί Φοιτητές"),
			)

	name = models.CharField(max_length=150, blank=True)
	faculty_en = models.CharField(max_length=150, blank=True, choices=FACULTY_CHOICES)
	faculty_el = models.CharField(max_length=150, blank=True, choices=FACULTY_CHOICES_GR)
	description = RichTextField(max_length=800, null=True, blank=True)
	email = models.EmailField(max_length=150, blank=True)
	cv_en = models.FileField(blank=True, upload_to='cv/', max_length=1500, null=True)
	cv_gr = models.FileField(blank=True, upload_to='cv/', max_length=1500, null=True)
	social = models.ForeignKey(Social, blank=True, null=True)
	image = models.ImageField(null=True, blank=True)
	address = models.CharField(max_length=150, blank=True, null=True)
	phone = models.CharField(max_length=150, blank=True, null=True)
	mobile = models.CharField(max_length=150, blank=True, null=True)
	order = models.IntegerField(blank=True, null=True, default=0)

	class Meta:
		verbose_name_plural = "People"

	def __str__(self):
		return str(self.name)

class Page(TimeStampedModel):
	title = models.CharField(max_length=150, blank=True, null=True)
	short_title = models.CharField(max_length=150, blank=True, null=True)
	long_title = models.CharField(max_length=150, blank=True, null=True)
	friendlyurl = models.SlugField(blank=True, null=True)
	order = models.IntegerField(blank=True)
	views = models.PositiveIntegerField(null=True, blank=True, default=0)
	
	class Meta:
		ordering = ['-order',]

	def __str__(self):
		return str(self.title)

#ALL THE CONTENTS ARE HERE
class Content(TimeStampedModel):
	CONTENT_CHOICES = (
						("Research", "Research"),
						("Publications", "Publications"),
						("Academic", "Academic"),
						("News", "News"),
					)

	SUB_CATEGORY_CHOICES = (
				("Areas", "Areas"),
				("Projects", "Projects"),
				("Conference Papers", "Conference Papers"),
				("Working Papers", "Working Papers"),
				("Journal Papers", "Journal Papers"),
				("Books", "Books"),
				("Courses", "Courses"),
				("Useful Links", "Useful Links"),
				("Software", "Software"),
			)

	SUB_SUB_CATEGORY_CHOICES = (
								("Scopus", "Scopus"),
								("Journals of OR/MS", "Journals of OR/MS"),
								("Journals of POM", "Journals of POM"),
								("Linear and integer Programming", "Linear and integer Programming"),
								("Decision Trees", "Decision Trees"),
								("Risk Management", "Risk Management"),
								("Multicriteria Analysis", "Multicriteria Analysis"),
								("Vehicle Routing", "Vehicle Routing"),
							)
	SUBJECT_CHOICES = (
				("Vehicle Routing Problems", "Vehicle Routing Problems"),
				("Scheduling Problems", "Scheduling Problems"),
				("Hazardous Material Logistical Problems", "Hazardous Material Logistical Problems"),
				("Green Vehicle Routing Problem", "Green Vehicle Routing Problem"),
				("Inventory Routing Problem", "Inventory Routing Problem"),
				("Green Inventory Routing Problem", "Green Inventory Routing Problem"),
			)

	LEVEL_CHOICES = (
				("Graduate", "Graduate"),
				("Undergraduate", "Undergraduate"),
			)

	content = models.CharField(max_length=150, blank=True, null=True, choices=CONTENT_CHOICES, default="Research Areas")
	sub_category = models.CharField(max_length=150, blank=True, null=True, choices=SUB_CATEGORY_CHOICES, default="Research")
	sub_sub_category = models.CharField(max_length=150, blank=True, null=True, choices=SUB_SUB_CATEGORY_CHOICES, default="Research")
	title = models.CharField(max_length=150, null=True, blank=True)
	funded = models.CharField(max_length=150, null=True, blank=True)
	subject = models.CharField(max_length=150, null=True, blank=True, choices=SUBJECT_CHOICES, default="Green Inventory Routing Problem")
	description = RichTextField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	author = models.CharField(max_length=1500, null=True, blank=True)
	location = models.CharField(max_length=1500, null=True, blank=True)
	url = models.URLField(null=True, blank=True)
	journal = models.CharField(max_length=1500, blank=True, null=True)
	volume = models.CharField(max_length=150, blank=True, null=True)
	number = models.CharField(max_length=150, blank=True, null=True)
	level = models.CharField(max_length=150, blank=True, null=True, choices=LEVEL_CHOICES, default="Graduate")
	year = models.IntegerField(null=True, blank=True, default=1994)
	duration = models.IntegerField(null=True, blank=True, default=1)
	publisher = models.CharField(max_length=150, blank=True, null=True)
	conference = models.CharField(max_length=150, blank=True, null=True)
	views = models.PositiveIntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return str(self.title)




