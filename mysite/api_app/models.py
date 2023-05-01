from django.db import models

class login_user(models.Model):
    log_user = models.CharField(max_length=50,blank=False, null=False)
    password = models.CharField(max_length=20,blank=False, null=False)
    # super_user = models.BooleanField(blank=False, null=True)
    def __str__(self):
        return self.log_user