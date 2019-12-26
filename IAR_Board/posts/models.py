from django.db import models

class AddPost(models.Model):
    postingTitle = models.CharField(max_length = 2000, verbose_name = "Title")
    city = models.CharField(max_length = 500, verbose_name = "City")
    postalCode = models.IntegerField(verbose_name = "Postal/Zip Code")
    description = models.TextField(help_text = '(please remember to put a price if needed)')
    email = models.EmailField(max_length = 500)
    phoneNumber = models.IntegerField(blank = True, verbose_name = "Phone Number")
    