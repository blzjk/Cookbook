import datetime
from django.db import models


class Categories(models.Model):
    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField()


class Ingredients(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"


class Recipes(models.Model):
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, max_length=255)
    ingredients = models.ManyToManyField(Ingredients)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(blank=True, upload_to='media')
    source = models.URLField(blank=True)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    reason = models.TextField()
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)


class Rating(models.Model):
    id = models.OneToOneField(Recipes, on_delete=models.CASCADE, primary_key=True)
    count = models.PositiveIntegerField(default=0)
    avg = models.FloatField(default=0)

    def AddVote(self, mark):
        if 0 <= mark <= 5:
            sum = self.count * self.avg
            sum = sum + mark
            self.count += 1
            self.avg = sum / self.count


