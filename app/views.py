from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render
from django.db.models import Q


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
            logo = form.cleaned_data['logo']
            companyName = form.cleaned_data['companyName']
            jobTitle = form.cleaned_data['jobTitle']
            jobLocation = form.cleaned_data['jobLocation']
            employmentType = form.cleaned_data['employmentType']
            seniorityLevel = form.cleaned_data['seniorityLevel']
            jobDescription = form.cleaned_data['jobDescription']
            models.PostJob.submit_job(logo, companyName, jobTitle, jobLocation,
                                      employmentType, seniorityLevel,
                                      jobDescription)
            return redirect('home')
        else:
            return render(request, 'post-job.html', {'form': form})


class AToZ(View):
    def get(self, request):
        return render(
            request, 'az.html',
            {'post_job': models.PostJob.objects.all().order_by('jobTitle')})


class NewOld(View):
    def get(self, request):
        return render(
            request, 'newold.html',
            {'post_job': models.PostJob.objects.all().order_by('-date')})


class OldNew(View):
    def get(self, request):
        return render(
            request, 'oldnew.html',
            {'post_job': models.PostJob.objects.all().order_by('date')})


class JobDetails(View):
    def get(self, request, id):
        return render(request, 'details.html',
                      {'post_job': models.PostJob.objects.get(id=id)})


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

class CommentDelete(View):
    def post(self, request, id):
        models.Comment.objects.get(id=id).delete()
        return redirect("admin")


class DeleteJob(View):
    def post(self, request, id):
        models.PostJob.objects.get(id=id).delete()
        return redirect('admin')
