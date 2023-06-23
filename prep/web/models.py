from django.core import exceptions
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator
from django.db import models



def validate_string_alphanumeric(value):
	for ch in value:
		if not ch.isalnum() and ch!= '_' not in value:
			raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


# Create your models here.
class Profile(models.Model):
	MIN_LEN_USERNAME=2
	MAX_LEN_USERNAME=15
	username=models.CharField(
		max_length=MAX_LEN_USERNAME,
		blank=False,
		null= False,
		validators=(MinLengthValidator(MIN_LEN_USERNAME), validate_string_alphanumeric)
	)
	email= models.EmailField(blank=False, null=False)
	age=models.PositiveIntegerField(blank=True, null=True)

class Album(models.Model):
	POP_MUSIC="Pop Music"
	JAZZ="Jazz Music"
	RNB="R&B Music"
	ROCK="Rock Music"
	COUNTRY="Country Music"
	DANCE="Dance Music"
	HIPHOP="Hip Hop Music"
	OTHER="Other"
	GENRE_CHOICES=(
		(POP_MUSIC, POP_MUSIC),
		(JAZZ,JAZZ),
		(RNB,RNB),
		(ROCK, ROCK),
		(COUNTRY, COUNTRY),
		(DANCE, DANCE),
		(HIPHOP, HIPHOP),
		(OTHER, OTHER),
	)

	album_name=models.CharField(blank=False, null=False, max_length=30, unique=True, verbose_name='Album Name',)
	artist= models.CharField(blank=False, null=False, max_length=30)
	genre=models.CharField(blank=False, null=False, max_length=30, choices=GENRE_CHOICES)
	description=models.TextField(blank=True, null=True)
	image_url=models.URLField(blank=True, null=True, verbose_name='Image URL',)
	price=models.FloatField(blank=False, null=False, validators=[MinValueValidator(0.0)])
	class Meta:
		ordering=('pk',)