from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from search.models import *
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.models import User,Group
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Register your models here.

class parcelAdmin(LeafletGeoAdmin):
	list_display = ('objectid','lr_number','shape_leng','shape_area')
	#default_lon =  4124488.98858
	#default_lat =  -62466.02641
	#default_zoom = 14

class searchAdmin (admin.ModelAdmin):
    list_display = ('app_id','first_name','last_name','email','telephone','date_applied','application_type','county','closest_town','status')
    search_fields = ['first_name','email'] 
    ordering = ['app_id']
    #readonly_fields = ['dc_comments ','upload_dcreport', 'final_comments']
    list_filter=('app_id','application_type')
    actions = ['send_EMAIL']


    def send_EMAIL(self, request, queryset):
        from django.core.mail import send_mail
        for i in queryset:
            if i.email:
                send_mail('Service Application', 'Hello,We aknowledge receipt of your application.It will be processed soon.', 'from@example.com',[i.email], fail_silently=False)
            else:
                self.message_user(request, "Mail sent successfully") 
    send_EMAIL.short_description = "Send an email to selected users"
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

class dataAdmin(admin.ModelAdmin):
	list_display = ('objectid','lr_number','registered_to','date_registered','registered_landuse','brokers','brokers_name','charged','caveat','loan','courtorder','timestamp') 
	ordering = ['objectid']
	prepopulated_fields = {"slug": ("lr_number",)}

admin.site.register(parcel, parcelAdmin)
admin.site.register(Data, dataAdmin)
admin.site.register(Search, searchAdmin)
#admin.site.register(UserProfile, userAdmin)

