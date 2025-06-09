from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MprfRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ]
    position = models.CharField(max_length=100, blank=True, null=True)
    vacancies = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.position}"
    
class MprfApply(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('interview', 'Interview Scheduled'),
        ('offer', 'Offer Made'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    ]
    mprf_request = models.ForeignKey(MprfRequest, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()

    img_candidate = models.ImageField(upload_to='images')

    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    # skills = models.ManyToManyField(Skills, blank=True)
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)

 

    def __str__(self):
        return f"{self.applicant_name} - {self.mprf_request.position}"
    

class EmployeeMaster(models.Model):


    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'In-Active'),]
    
    # ref fields
    application_id = models.ForeignKey(MprfApply, on_delete=models.CASCADE,null=True, blank=True)
    mprf_request = models.ForeignKey(MprfRequest, on_delete=models.CASCADE,null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()

    img_candidate = models.ImageField(upload_to='images')

    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    # skills = models.ManyToManyField(Skills, blank=True)
    resume = models.FileField(upload_to='resumes')
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.applicant_name}"



