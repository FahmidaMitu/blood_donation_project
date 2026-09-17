from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import DonorProfile, BloodRequest
from .forms import UserRegisterForm, DonorProfileForm, BloodRequestForm

def home(request):
    return render(request, 'core/home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Donor Views
def donor_list(request):
    donors = DonorProfile.objects.all()
    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    availability = request.GET.get('availability')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)
    if location:
        donors = donors.filter(location__icontains=location)
    if availability:
        donors = donors.filter(availability=availability)

    return render(request, 'core/donor_list.html', {'donors': donors})

def donor_detail(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)
    return render(request, 'core/donor_detail.html', {'donor': donor})

@login_required
def create_or_edit_donor_profile(request):
    profile, created = DonorProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = DonorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Donor Profile updated successfully!")
            return redirect('donor_detail', pk=profile.pk)
    else:
        form = DonorProfileForm(instance=profile)
    return render(request, 'core/donor_form.html', {'form': form})

# Blood Request Views
def request_list(request):
    requests_list = BloodRequest.objects.all().order_by('-created_at')
    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    status = request.GET.get('status')

    if blood_group:
        requests_list = requests_list.filter(blood_group=blood_group)
    if location:
        requests_list = requests_list.filter(location__icontains=location)
    if status:
        requests_list = requests_list.filter(status=status)

    return render(request, 'core/request_list.html', {'requests': requests_list})

def request_detail(request, pk):
    req = get_object_or_404(BloodRequest, pk=pk)
    return render(request, 'core/request_detail.html', {'req': req})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_req = form.save(commit=False)
            blood_req.requester = request.user
            blood_req.save()
            messages.success(request, "Blood Request created!")
            return redirect('request_list')
    else:
        form = BloodRequestForm()
    return render(request, 'core/request_form.html', {'form': form, 'title': 'Create Blood Request'})

@login_required
def edit_request(request, pk):
    req = get_object_or_404(BloodRequest, pk=pk, requester=request.user)
    if request.method == 'POST':
        form = BloodRequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            messages.success(request, "Request updated!")
            return redirect('request_detail', pk=req.pk)
    else:
        form = BloodRequestForm(instance=req)
    return render(request, 'core/request_form.html', {'form': form, 'title': 'Edit Blood Request'})

@login_required
def delete_request(request, pk):
    req = get_object_or_404(BloodRequest, pk=pk, requester=request.user)
    if request.method == 'POST':
        req.delete()
        messages.success(request, "Request deleted!")
        return redirect('my_requests')
    return render(request, 'core/request_confirm_delete.html', {'req': req})

@login_required
def my_requests(request):
    user_requests = BloodRequest.objects.filter(requester=request.user)
    return render(request, 'core/my_requests.html', {'requests': user_requests})