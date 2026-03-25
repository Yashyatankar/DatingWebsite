# ClientInfo/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # ✅ always points to login.User via AUTH_USER_MODEL

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('O', 'Other'),
    ]

    INTERESTED_IN = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('O', 'Others'),
    ]

    INTEREST_CHOICES = [
        ('MOVIES', 'Movies & Cinema'),
        ('MUSIC', 'Music & Concerts'),
        ('GAMING', 'Video Games'),
        ('ANIME', 'Anime & Manga'),
        ('COOKING', 'Cooking & Baking'),
        ('TRAVEL', 'Traveling'),
        ('READING', 'Reading & Literature'),
        ('PHOTOGRAPHY', 'Photography'),
        ('ART', 'Art & Design'),
        ('GYM', 'Fitness & Gym'),
        ('HIKING', 'Hiking & Outdoors'),
        ('YOGA', 'Yoga & Wellness'),
        ('SPORTS', 'Sports'),
        ('DANCING', 'Dancing'),
        ('COFFEE', 'Coffee & Tea'),
        ('WINE', 'Wine & Spirits'),
        ('VEGAN', 'Vegan/Vegetarian Lifestyle'),
        ('FOODIE', 'Trying New Restaurants'),
        ('TECH', 'Technology & Gadgets'),
        ('CODING', 'Coding & Open Source'),
        ('SCIENCE', 'Science & Space'),
    ]

    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    bio           = models.TextField(blank=True)
    age           = models.IntegerField()
    gender        = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interested_in = models.CharField(max_length=6, choices=INTERESTED_IN, default='M')
    interests     = models.TextField(blank=True, default='')
    location      = models.CharField(max_length=100)
    photo         = models.ImageField(upload_to='photos/')

    def get_interests_list(self):
        if self.interests:
            return self.interests.split(',')
        return []

    def set_interests_list(self, interests_list):
        self.interests = ','.join(interests_list)

    def __str__(self):
        return f"{self.user.username} - {self.age}"


