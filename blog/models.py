from django.db import models

# Create your models here.

class Category(models.Model):
    """Модель категории"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name
    """возаращает читабельное имя категории, которое было создано из админпанели, вместо CategoryObject"""

    class Meta:
        verbose_name = "Категория" """единственное число"""
        """меняет имя с английского на русский"""

        verbose_name_plural = "Категории" """множественное число"""
        """изменяет окончание на множественное (убирает букву 's' с конца "Категорииs")"""




