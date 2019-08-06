from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    mp4file = models.FileField(upload_to='mp4videos/', null=True, verbose_name="")


    def __str__(self):
        return self.name + ": " + str(self.videofile)

class AllMedia(models.Model):
    FILE_TYPES = (
        ('I', 'Image'),
        ('V', 'Video'),
        ('A', 'Audio'),
    )
    name = models.CharField(max_length=60)
    media_file = models.FileField(upload_to='videos/media_file/', null=True, verbose_name="")
    file_types = models.CharField(max_length=1, choices=FILE_TYPES)
