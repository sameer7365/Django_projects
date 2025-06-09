from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Department, MprfRequest,Skills, MprfApply,EmployeeMaster


# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')

def signup(request):
    """
    Render the signup page.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if username and password and confirm_password:
            if password == confirm_password:
                try:
                    User.objects.get(username=username)
                    return HttpResponse("Username already exists.")
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, "User created successfully.")
                    return redirect('login')
            else:
                return HttpResponse("Passwords do not match.")
        else:
            return HttpResponse("Please fill in all fields.")
    return render(request, 'signup.html')

def login(request):
    """
    Render the login page.
    """
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user:
                    return HttpResponse("Username is Invalid.")
                check_password = user.check_password(password)
                if check_password:
                    request.session['username'] = username
                    if user.groups.filter(name='Admin').exists():
                        return redirect("dash")
                    else:
                        val = EmployeeMaster.objects.get(user_id=user)
                        return redirect("employeeform",pk=val.pk)
                else:
                    return HttpResponse("Invalid credentials, please try again.")
            except User.DoesNotExist:

                return HttpResponse("Username does not exist.")
        else:
            return HttpResponse("Please enter both username and password.")
    return render(request, 'login.html')


def dash(request):
    return render(request, 'dashboard.html')

def mprfform(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        vacancies = request.POST.get('vacancies')
        department_id = request.POST.get('department')
        location = request.POST.get('location')
        job_description = request.POST.get('job_description')
        requirements = request.POST.get('requirements')

        if position and department_id and vacancies and location:
            try:
                department = Department.objects.get(id=department_id, is_active=True)
                # Assuming MprfRequest is a model that needs to be created
                MprfRequest.objects.create(
                    position=position, 
                    department=department, 
                    vacancies=vacancies, 
                    location=location,
                    job_description=job_description,
                    requirements=requirements,)
                messages.success(request, "MPRF Request submitted successfully.")
                return redirect('success')
            except Department.DoesNotExist:
                messages.error(request, "Invalid department selected.")
        else:
            messages.error(request, "Please fill in all fields.")
    else:
        context = {
            'departments': Department.objects.filter(is_active=True)
        }
        return render(request, 'mprf-form.html',context)
    
def AppliedCandidates(request):
    status_filter = request.GET.get('status')
    print("print get method called",status_filter)
    if status_filter:
        candidates = MprfApply.objects.filter(status=status_filter)
    else:
        candidates = MprfApply.objects.all()

    # candidates = MprfApply.objects.all()
    print("list_applied_candidates",candidates)
    status_choices = MprfApply.STATUS_CHOICES
    print("status_choices",status_choices)

    context ={'candidates': candidates,
            'request': request ,
              'status_choices':status_choices}
    return render(request,'listviewapplied.html',context)

def formviewapplied(request,pk):
    print("pk",pk)
    candidate = MprfApply.objects.get(pk=pk)
    context = {
        'candidate': candidate,
    }
    return render(request, 'formviewapplied.html', context)




# def AppliedCandidatesStatus(request,pk):


    
def success(request):
    """
    Render the success page after form submission.
    """
    return render(request, 'success.html')

def jobs(request):
    """
    Render the jobs page to view all MPRF requests.
    """
    mprf_requests = MprfRequest.objects.all()
    context = {
        'mprf_requests': mprf_requests
    }
    return render(request, 'jobs.html', context)

def mprfauthform(request,pk):
    print(pk)
    mprfapplyform = MprfRequest.objects.filter(id=pk).first()
    print(777777777777777777,mprfapplyform.id)
    """
    Render the MPRF application form for authenticated users.
    """
    # if request.method == 'POST':
    #     applicant_name = request.POST.get('applicant_name')
    #     applicant_email = request.POST.get('applicant_email')
    #     cover_letter = request.POST.get('cover_letter')

    #     if applicant_name and applicant_email and cover_letter:
    #         try:
    #             mprf_apply = MprfApply.objects.create(
    #                 applicant_name=applicant_name,
    #                 applicant_email=applicant_email,
    #                 cover_letter=cover_letter
    #             )
    #             mprf_apply.save()
    #             messages.success(request, "Application submitted successfully.")
    #             return redirect('success')
    #         except Exception as e:
    #             messages.error(request, f"Error submitting application: {e}")
    #     else:
    #         messages.error(request, "Please fill in all fields.")
    
    return render(request, 'apply-authform.html', {'mprfapplyform': mprfapplyform})

def mprfapplyform(request,pk):
    print(pk)
    mprfapplyform = MprfRequest.objects.get(id=pk)
    uid = request.GET.get('uid')
    if uid:
        user = User.objects.filter(id=uid).first()  
    context = {
        'mprfapplyform': mprfapplyform,
        'skills': Skills.objects.all(),
        'user': user
    }
    already_applied = False
    # if request.user.is_authenticated:
    already_applied = MprfApply.objects.filter(
        mprf_request=mprfapplyform,
        user_id=user)
    if already_applied:
        already_applied_status = already_applied.first()
        already_created_date = already_applied.first().applied_on

        already_applied = True
        print("already_applied", already_applied)
        # already_applied_obj = already_applied.first()
        # already_applied_status = already_applied_obj.status
        # print("already_applied_status", already_applied_status)
    context = {
        # 'mprf_request': mprf_request,
        'mprfapplyform': mprfapplyform,
        'user': user,
        'already_applied': already_applied,
        'already_applied_status': already_applied_status if already_applied else None,
        'already_created_date': already_created_date if already_applied else None,
    }

    if request.method == 'POST':
        print("request.POST")
        applicant_name = request.POST.get('applicant_name')
        applicant_email = request.POST.get('applicant_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        pan_no = request.POST.get('pan_number')
        aadhar_no = request.POST.get('aadhaar_number')
        bank_acc_no = request.POST.get('bank_account')
        ifsc = request.POST.get('ifsc_code')
        emergency_ph = request.POST.get('emergency_contact')
        # img_candidate =request.POST.get('img_candidate')
        # resume = request.POST.get('resume')
        cover_letter = request.POST.get('cover_letter')
        # ✅ Get files from request.FILES
        img_candidate = request.FILES.get('img_candidate')
        resume = request.FILES.get('resume')

        print("img_candidate >>>",img_candidate)
        print("resume >>>",resume)
        

        if not cover_letter:
            cover_letter = '--'
        if applicant_name and applicant_email and cover_letter:
            try:
                mprf_apply = MprfApply.objects.create(
                    mprf_request=mprfapplyform,
                    user_id=user,
                    applicant_name=applicant_name,
                    applicant_email=applicant_email,
                    img_candidate = img_candidate,
                    phone = phone,
                    address = address,
                    date_of_birth = date_of_birth,
                    gender = gender,
                    resume = resume,
                    emergency_contact = emergency_ph,
                    pan_number = pan_no,
                    aadhaar_number = aadhar_no,
                    bank_account = bank_acc_no,
                    ifsc_code = ifsc,
                    cover_letter=cover_letter
                )
                mprf_apply.save()
                messages.success(request, "Application submitted successfully.")
                return redirect('success')
            except Exception as e:
                messages.error(request, f"Error submitting application: {e}")
        else:
            messages.error(request, "Please fill in all fields.")         

    return render(request, 'mprfapply.html',context)
    # return render(request, 'signup.html',context)

def loginapply(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(8888888888,request.POST.get('mprfid'))
        pk = request.POST.get('mprfid')

        if username and password:
            try:
                user = User.objects.get(username=username)
                print(9999999999999999,user)
                if not user:
                    return HttpResponse("Username is Invalid.")
                check_password = user.check_password(password)
                if check_password:
                    request.session['username'] = username
                     # Build full URL with query param
                    url = reverse('mprfapplyform', kwargs={'pk': pk})
                    full_url = f"{url}?uid={user.id}"
                    return redirect(full_url)
                    # return redirect("mprfapplyform", pk=pk) + f"?uid={user.id}"

                    # return redirect("mprfapplyform", pk=pk)
                else:
                    return HttpResponse("Invalid credentials, please try again.")
            except User.DoesNotExist:
                return HttpResponse("Username does not exist.")
        else:
            return HttpResponse("Please enter both username and password.")
    return HttpResponse("Please login to apply for the job.")

def signupapply(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        confirm_password = request.POST.get('new_password')
        # confirm_password = request.POST.get('password2')
        pk = request.POST.get('mprfid')

        if username and confirm_password:
            if confirm_password:
                try:
                    User.objects.get(username=username)
                    return HttpResponse("Username already exists.")
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, password=confirm_password)
                    user.save()
                    messages.success(request, "User created successfully.")
                    request.session['username'] = username
                    # Build full URL with query param
                    url = reverse('mprfapplyform', kwargs={'pk': pk})
                    full_url = f"{url}?uid={user.id}"
                    return redirect(full_url)
            else:
                return HttpResponse("Passwords do not match.")
        else:
            return HttpResponse("Please fill in all fields.")
    return HttpResponse("Please signup to apply for the job.")


def update_candidate_status(request, pk):
    if request.method == 'POST':
        update_status = request.POST.get('status')
        val = MprfApply.objects.filter(pk=pk).first()
        if update_status == 'accepted':
            application_instance = val  

            # Get related instances
            mprf_request_instance = application_instance.mprf_request
            user_instance = application_instance.user_id

            # creation of employee 
            employee = EmployeeMaster.objects.create(
                application_id=application_instance,
                mprf_request=mprf_request_instance,
                user_id=user_instance,
                applicant_name=application_instance.applicant_name,
                applicant_email=application_instance.applicant_email,
                img_candidate=application_instance.img_candidate, 
                phone=application_instance.phone,
                address=application_instance.address,
                date_of_birth=application_instance.date_of_birth,
                gender=application_instance.gender,
                resume=application_instance.resume,               
                cover_letter=application_instance.cover_letter,
                applied_on=application_instance.applied_on,
                status='active',
                emergency_contact=application_instance.emergency_contact,
                pan_number=application_instance.pan_number,
                aadhaar_number=application_instance.aadhaar_number,
                bank_account=application_instance.bank_account,
                ifsc_code=application_instance.ifsc_code,
            )
            employee.save()
        val.status = update_status
        val.save()  

    return redirect('AppliedCandidates')


def employeelist(request):
    print("employeelist called !!")

    candidates = EmployeeMaster.objects.all()

    context = {'candidates':candidates}



    # return HttpResponse("employye list view opened")
    return render(request,'employeelist.html',context)


def employeeform(request,pk):
    print("gggg",pk)

    # EmployeeMaster.objects.all()
    candidate = EmployeeMaster.objects.get(pk=pk)
    context = {
        'candidate': candidate,
    }
    return render(request, 'employeedash.html', context)




   


