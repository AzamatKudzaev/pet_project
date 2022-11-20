from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """
    MALE = 'M'
    FAMALE = "F"
    CURRENCY_CHOICES = [  # а причем тут валюта? названия переменных должны быть осмысленными
        (MALE, 'Male'),
        (FAMALE, 'Famele')
    ]

    и в целом это какая-то бессмысленная конструкция - можно сделать лакончинее и понятнее
    """

    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    # обоснуй, зачем указывать null=True для полей выше

    mail = models.EmailField(max_length=254)

    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(150)])
    about_me = models.TextField(max_length=500)
    # но в age и about me null нет

    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    # а почему тут бланк?

    registration_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_name": self.first_name})


class Article(models.Model):
    """
    та же хуйня, что и в прошлой модели


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
    """

    ARTICLES_CHOICES = (
        (0, 'Not selected'),
        (1, 'Scientific'),
        (2, 'Review'),
        (3, 'Informational')
    )

    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True  # article's author
    )
    title = models.CharField(max_length=80)
    text = models.TextField(max_length=999, blank=True)
    publication = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    article_views = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    article_likes = models.IntegerField(blank=True, null=True, default=0)
    article_dislikes = models.IntegerField(blank=True, null=True, default=0)
    article_kind = models.SmallIntegerField(
        # да, small integer тоже можно использовать.
        # в данном случае это даже удобнее
        choices=ARTICLES_CHOICES,
        default=0
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show-article", kwargs={"id_article": self.pk, "article_kind": self.article_kind})
