from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
# Create your models here.


class Profile(models.Model):
    MALE = 'M'
    FAMALE = "F"
    CURRENCY_CHOICES = [
        (MALE, 'Male'),
        (FAMALE, 'Famele')

    ]

    sex = models.CharField(max_length=1, choices=CURRENCY_CHOICES, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    mail = models.EmailField(max_length=254)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(150)])
    about_me = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    registration_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_name": self.first_name})


class Article(models.Model):
    NOT_SELECTED = 'not selected'
    SCINEFIC = 'scinefic'
    REVIEW = 'review'
    INFORMATIONAL = 'informational'

    ARTICLES_KINDS = {
        (NOT_SELECTED, 'Not selected'),
        (SCINEFIC, 'Scientific'),
        (REVIEW, 'Review'),
        (INFORMATIONAL, 'Informational')
    }

    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)  # article's author
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=999, blank=True)
    publication = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)  
    change_date = models.DateTimeField(auto_now=True)
    article_views = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    article_likes = models.IntegerField(blank=True, null=True, default=0)
    article_dislikes = models.IntegerField(blank=True, null=True, default=0)
    article_kind = models.CharField(
        max_length=20,
        choices=ARTICLES_KINDS,
        default=NOT_SELECTED
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show-article", kwargs={"id_article": self.pk, "article_kind": self.article_kind})
