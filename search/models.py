from django.db import models
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,Group
import datetime 

status = (
    ('Unchecked','Unchecked'),
    ('Checked','Checked'),
    ('Closed','Closed'),

    )
application_types=(
            ('Search','Search'),
            ('Register','Register'),
            
    )
county = (
    ('Nyeri','Nyeri'),
    ('Kirinyaga','Kirinyaga'),
    ('Kiambu','Kiambu'),
    ('Laikipia','Laikipia'),

    )
# Create your models here.
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today()) 
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='User profiles'
        
class parcel(models.Model):
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    lr_number = models.CharField(max_length=100, null=True)
    #designated = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return unicode(self.lr_number) or u''

class Search(models.Model):
    user = models.OneToOneField(User)
    app_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50, help_text='user@user.com')
    telephone = models.CharField(max_length=50, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)
    application_type = models.CharField(max_length=50, choices=application_types)
    county = models.CharField(max_length=50, choices=county)
    Area_Name=models.CharField(max_length=15,null=True)
    closest_town=models.CharField(max_length=15,null=True)
    description = models.TextField(max_length=256)
    status = models.CharField(max_length=15, null=False, choices=status, default=status[0][0])
    
    def __unicode__(self):
        return self.email

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

    class Meta:
        verbose_name_plural = "Applied Services" 
        managed = True


class Data(models.Model):
    objectid = models.OneToOneField(parcel, related_name = 'parcels')
    lr_number = models.CharField(max_length=100, null=False)
    registered_to = models.CharField(max_length=256)
    area = models.FloatField()
    date_registered = models.DateTimeField()
    registered_landuse = models.CharField(max_length=50)
    brokers = models.BooleanField()
    brokers_name = models.CharField(max_length=256, blank=True)
    #restrictions = models.CharField(choices= choices, null=False, blank=False)
    charged =models.BooleanField()
    caveat = models.BooleanField()
    loan = models.BooleanField()
    courtorder = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Parcel Data'

    def get_absolute_url(self):
        return reverse("parcel_detail", kwargs={"slug": self.slug})

    
