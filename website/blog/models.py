from django.db import models
from django.contrib.auth.models import User

###########################################

class Blog(models.Model):

    title = models.CharField( max_length=255)
    post_type=models.CharField(max_length= 30)
    description = models.TextField( null= True , blank=True , max_length=300)
    image = models.ImageField(upload_to= 'images' ,blank=True , default='images/gal_6.jpg')
    created_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True ,blank=True )

    def __str__(self):
        return self.title
    ########## show the 
    class Meta:

        ordering = ['-created_at']

