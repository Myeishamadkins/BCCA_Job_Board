from django import forms


class PostJobForm(forms.Form):
    companyName = forms.CharField(label="Company Name:")
    jobTitle = forms.CharField(label="Job Title:")
    jobLocation = forms.CharField(label="Job Location:")
    employmentType = forms.CharField(label="Employment Type")
    seniorityLevel = forms.CharField(label="Seniority Level")
    jobDescription = forms.CharField(
        label="Job Description",
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your job description here'}))
