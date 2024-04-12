from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField(blank=True, null=True)
    method = models.TextField()
    prep_time = models.CharField(max_length=100)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# class Cures(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(max_length=2)
#     weight = models.IntegerField(max_length=5)
#     height = models.IntegerField(max_length=3)
#     country = models.CharField(max_length=100)
#     disease = models.CharField(max_length=100)
#     allergies = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name