from django.db import models


class UserDetails(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    age = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "UserDetails"


class UserActivities(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    request_type = models.CharField(max_length=200, null=False)
    keywords = models.CharField(max_length=200, null=False, default='form values')
    terminal = models.CharField(max_length=200, null=False)
    request_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "UserActivities"
