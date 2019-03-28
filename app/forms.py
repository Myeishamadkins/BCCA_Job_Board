from django import forms


class PostJobForm(forms.Form):
    logo = forms.URLField(label="logo")
    companyName = forms.CharField(label="Company Name:")
    jobTitle = forms.CharField(label="Job Title:")
    jobLocation = forms.CharField(label="Job Location:")
    employmentType = forms.CharField(label="Employment Type:")
    seniorityLevel = forms.CharField(label="Seniority Level:")
    jobDescription = forms.CharField(
        label="Job Description",
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your job description here'}))


class CommentForm(forms.Form):
    name = forms.CharField(label='Name:')
    comment = forms.CharField(
        label='Comment:',
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter your comment here...'}))
