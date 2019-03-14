from django import forms


class PostJobForm(forms.Form):
    companyName = forms.CharField(label="Company Name:")
    jobTitle = forms.CharField(label="Job Title:")
    jobLocation = forms.CharField(label="Job Location:")
    employmentType = forms.CharField(label="Employment Type:")
    seniorityLevel = forms.CharField(label="Seniority Level:")
    jobDescription = forms.CharField(
        label="Job Description",
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your job description here'}))


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name:')
    email = forms.EmailField(label='Email:')
    phoneNumber = forms.CharField(label='Phone Number:')
    companyNote = forms.CharField(
        label='Note to Company:',
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your note here...'}))
