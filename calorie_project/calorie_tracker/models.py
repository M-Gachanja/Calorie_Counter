from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    date_consumed = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.calories} calories"

    class Meta:
        ordering = ['-date_consumed', '-created_at']