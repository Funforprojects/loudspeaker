from django.db import models

class album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)

    def __str__(self):
        return self.album_title

class song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_album=models.ForeignKey(album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.song_title