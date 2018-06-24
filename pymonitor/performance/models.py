from django.db import models

#Create your models here.
class Performance(models.Model):
    server = models.CharField(max_length=255)
    file_system = models.CharField(max_length=255)
    total_size = models.CharField(max_length=255)
    use_percentage = models.CharField(max_length=255)
    free_space = models.CharField(max_length=255)
    used_space = models.CharField(max_length=255)
    load = models.CharField(max_length=255)
    available_memory = models.CharField(max_length=255)
    cache_memory = models.CharField(max_length=255)
    free_memory = models.CharField(max_length=255)
    shared_memory = models.CharField(max_length=255)
    total_memory = models.CharField(max_length=255)
    used_memory = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_performance'