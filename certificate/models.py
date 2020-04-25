from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL


class Firm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    director = models.CharField(max_length=50, null=True)
    nip = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s/%s.%s" %("profile", instance.user.username, instance.user.username, extension)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firm = models.OneToOneField(Firm, on_delete=models.CASCADE)
    signature = models.ImageField(upload_to=upload_location, 
                null=True,
                blank=True, 
                width_field=None, 
                height_field=None)
    position = models.CharField(max_length=30)
    sap_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    leave_date = models.DateField(auto_now=False)
    leave_hour = models.TimeField(auto_now_add=False)
    return_hour = models.TimeField(auto_now_add=False, blank=True, null=True)
    accept = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " -- " + self.user.profile.position + " -- " + str(self.leave_date)

    def get_absolute_url(self):
        return "/certificate/{}".format(self.id)

    def get_accept_url(self):
        return "/certificate/{}/accept".format(self.id)
    
    def get_delete_url(self):
        return "/certificate/{}/delete".format(self.id)

    def get_pdf_url(self):
        return "/certificate/{}/pdf".format(self.id)

    def get_download_pdf_url(self):
        return "/certificate/{}/downloadpdf".format(self.id)