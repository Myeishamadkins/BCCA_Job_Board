from django.db import models

# Create your models here.


class PostJob(models.Model):
    companyName = models.TextField()
    jobTitle = models.TextField()
    jobLocation = models.TextField()
    employmentType = models.TextField()
    seniorityLevel = models.TextField()
    jobDescription = models.TextField()

    def __str__(self):
        return '''
        Company Name: {}
        Job Title: {}
        Job Location: {}
        Employment Type: {}
        Seniority Level: {}
        Job Description: {}
        '''.format(self.companyName, self.jobTitle, self.jobLocation,
                   self.employmentType, self.seniorityLevel,
                   self.jobDescription)

    @staticmethod
    def submit_job(companyName, jobTitle, jobLocation, employmentType,
                   seniorityLevel, jobDescription):
        PostJob(
            companyName=companyName,
            jobTitle=jobTitle,
            jobLocation=jobLocation,
            employmentType=employmentType,
            seniorityLevel=seniorityLevel,
            jobDescription=jobDescription).save()


class Application(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phoneNumber = models.TextField()
    companyNote = models.TextField()
    post_job = models.ForeignKey(PostJob, on_delete=models.PROTECT)

    def __str__(self):
        return '''
        Name: {}
        Email: {}
        Phone Number: {}
        Note to Company: {}
        Application for Job: {}
        '''.format(self.name, self.email, self.phoneNumber, self.companyNote,
                   self.post_job)

    @staticmethod
    def submit_app(name, email, phoneNumber, companyNote, post_job_id):
        Application(
            name=name,
            email=email,
            phoneNumber=phoneNumber,
            companyNote=companyNote,
            post_job_id=post_job_id).save()

