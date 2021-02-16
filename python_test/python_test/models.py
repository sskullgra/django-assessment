# Insert models here
from django.db import models

class Client(models.Model):
    #a client name
    name = models.CharField(max_length=50, unique=True)
    #a contact name
    contact = models.CharField(max_length=50)
    #an email address
    email = models.EmailField(max_length=255)
    #a phone number
    phone = models.CharField(max_length=50)
    #their address (as street name, suburb, postcode and state)
    address_street = models.CharField(max_length=255)
    address_suburb = models.CharField(max_length=255)
    address_postcode = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
