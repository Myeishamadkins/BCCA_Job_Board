from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, 'home.html',
                      {'post_job': models.PostJob.objects.all()})


class PostJob(View):
    def get(self, request):
        return render(request, 'post-job.html', {'form': forms.PostJobForm()})

    def post(self, request):
        form = forms.PostJobForm(data=request.POST)
        if form.is_valid():
            companyName = form.cleaned_data['companyName']
            jobTitle = form.cleaned_data['jobTitle']
            jobLocation = form.cleaned_data['jobLocation']
            employmentType = form.cleaned_data['employmentType']
            seniorityLevel = form.cleaned_data['seniorityLevel']
            jobDescription = form.cleaned_data['jobDescription']
            models.PostJob.submit_job(companyName, jobTitle, jobLocation,
                                      employmentType, seniorityLevel,
                                      jobDescription)
            return redirect('home')
        else:
            render(request, 'post-job.html', {'form': form})


class JobDetails(View):
    def get(self, request, id):
        return render(request, 'details.html',
                      {'post_job': models.PostJob.objects.get(id=id)})


class ApplyToJob(View):
    def get(self, request, id):
        return render(request, 'apply.html', {'form': forms.ApplicationForm()})

    def post(self, request, id):
        form = forms.ApplicationForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phoneNumber']
            companyNote = form.cleaned_data['companyNote']
            models.Application.submit_app(name, email, phoneNumber,
                                          companyNote, id)
            return redirect('home')
        else:
            return render(request, 'apply.html', {'form': form})


class Comment(View):
    def get(self, request, id):
        return render(request, 'comment.html', {'form': forms.CommentForm()})

    def post(self, request, id):
        form = forms.CommentForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            models.Comment.submit_comment(name, comment, id)
            return redirect('home')
        else:
            return render(request, 'comment.html', {'form': form})


class Admin(View):
    def get(self, request):
        return render(request, 'admin.html',
                      {'post_job': models.PostJob.objects.all()})
