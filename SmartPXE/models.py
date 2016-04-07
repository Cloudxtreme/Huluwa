from django.db import models


class OS(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    tftp_ip = models.CharField(max_length=15)


class Client(models.Model):
    # PXE client
    mac = models.CharField(max_length=17)  # for PXE boot usage
    hostname = models.CharField(max_length=30)  # for display only
    console_ip = models.CharField(max_length=15)
    console_username = models.CharField(max_length=30)
    console_password = models.CharField(max_length=30)
