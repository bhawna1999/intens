from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from .forms import ContactForm,EnquiryForm,PartnerForm


# # Create your views here.
# def base(request):
# 	return render(request = request,
# 				   template_name = 'base.html')
	
def homepage(request):
	return render(request = request,
				  template_name = "home.html",
				  # context = {"jobs" : Job.objects.all}
				  )

def about(request):
	return render(request = request,
		 		  template_name = "about.html",
				  # context = {"jobs" : Job.objects.all}
				  )

def employer(request):

	if request.method=='POST':
		form = EnquiryForm(request.POST)
		if form.is_valid():
			form.save()

	form = EnquiryForm()
	return render(request,'employer.html',{'form':form} )

def partner(request):
	
	if request.method=='POST':
		form = PartnerForm(request.POST)
		if form.is_valid():
			form.save()

	form = PartnerForm()
	return render(request,'partner.html',{'form':form} )



def contact_us(request):

	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

	form = ContactForm()
	return render(request,'contact.html',{'form':form} )



def log_sign(request):
	return render(request = request,
				  template_name = "log_sign.html",
				  # context = {"jobs" : Job.objects.all}
				  )	

def candidate(request):
	return render(request = request,
				  template_name = "candidate.html",
				  # context = {"jobs" : Job.objects.all}
				  )


def jobs(request):
	# job1 = Job()
	# job1.job_title = 'Web dev'
	# job1.job_des = 'ABC Education'
	# job1.job_sal = 20000
	# job1.job_loc = 'Delhi'

	# job2 = Job()
	# job2.job_title = 'Devops'
	# job2.job_des = 'ABC Education'
	# job2.job_sal =10000
	# job2.job_loc = 'New Delhi'

	# job3 = Job()
	# job3.job_title = 'Web developer'
	# job3.job_des = 'ABC Education'
	# job3.job_sal = 25000
	# job3.job_loc = 'Banglore'
	
	# job4 = Job()
	# job4.job_title = 'Web developer'
	# job4.job_des = 'ABC Education'
	# job4.job_sal = 25000
	# job4.job_loc = 'Banglore'

	# jobArr = [job1, job2, job3, job4]

	jobArr = Job.objects.all()
	return render(request = request,
				  template_name = "jobs.html",
				  context = {'jobArr' : jobArr}
				  )

def apply(request):
	return render(request = request,
				  template_name = "apply.html",
				  # context = {"jobs" : Job.objects.all}
				  )
def patcomm(request):
	return render(request = request,
				  template_name = "patcomm.html",
				  # context = {"jobs" : Job.objects.all}
				  )