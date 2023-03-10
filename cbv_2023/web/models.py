from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    seniority_level = models.CharField(
        max_length=15,
        choices=(
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
            ('Senior', 'Senior'),
        )
    )

    def get_absolute_url(self):
        pass
