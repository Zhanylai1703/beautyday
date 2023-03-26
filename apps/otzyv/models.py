from django.db import models


QUALITY_CHOICES = (
    ("плохое", "плохое"),
    ("среднее", "среднее"),
    ("удовлетворительное", "удовлетворительное"),
    ("хорошее", "хорошее"),
    ("отличное", "отличное"),
)


ATMOSPHERE_CHOICES = (
    ("плохая", "плохая"),
    ("средняя", "средняя"),
    ("удовлетворительная", "удовлетворительная"),
    ("хорошая", "хорошая"),
    ("отличная", "отличная"),
)


class Review(models.Model):
    name = models.CharField(
        max_length=100, 
        blank=False, 
        verbose_name='имя',
    )
    description = models.TextField(
        blank=False, 
        verbose_name='отзыв',
    )
    quality = models.CharField(
        max_length=20, 
        choices = QUALITY_CHOICES , 
        default = "удовлетворительное", 
        verbose_name='качество',
    )
    atmosphere = models.CharField(
        max_length=20, 
        choices = ATMOSPHERE_CHOICES, 
        default = "удовлетворительная", 
        verbose_name='атмосфера',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        