from django.contrib import admin
from .models import Job
from .models import Contact,Enquiry,Partner

# Register your models here.
class JobAdmin(admin.ModelAdmin):
	fields = [
				"job_title",
				"job_des",
				"job_sal", 
				"job_loc"
				]

admin.site.register(Job , JobAdmin)

admin.site.register(Contact)
admin.site.register(Enquiry)
admin.site.register(Partner)
