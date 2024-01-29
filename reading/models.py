from django.db import models


class Reading(models.Model):
    title = models.CharField("本のタイトル", max_length=30)
    writer = models.CharField("筆者", max_length=30)
    memo = models.TextField("メモ", blank=True)
    date = models.DateField("読了日")

    def __str__(self):
        return self.title
