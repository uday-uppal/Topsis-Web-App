from django.db import models

# Create your models here.
class topsis_data(models.Model):
    dataset=models.FileField(upload_to='topsis_data_store/')
    weights=models.CharField(max_length=1000)
    impacts=models.CharField(max_length=1000)
    email=models.EmailField()

    def __str__(self):
        return self.email
