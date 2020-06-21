from django import forms
from .models import Contact
from .models import Enquiry,Partner

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','mail','contactNumber','message')
        widgets={
                'message':forms.Textarea(attrs={'rows' : 4, 'cols' : 23})
        }

class EnquiryForm(forms.ModelForm):
    class Meta :
        model = Enquiry
        fields = ('name','contactNumber','company','post','city','description')
        widgets={
                'description':forms.Textarea(attrs={'rows' : 4, 'cols' : 23})
        }

class PartnerForm(forms.ModelForm):
    class Meta :
        model = Partner
        fields = ('organisationType','organisationName','name','email','contactNumber','experience')
