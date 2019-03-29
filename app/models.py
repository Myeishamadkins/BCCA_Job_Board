from django.db import models


class PostJob(models.Model):
    logo = models.URLField()
    date = models.DateTimeField(auto_now=True)
    companyName = models.TextField()
    jobTitle = models.TextField()
    jobLocation = models.TextField()
    employmentType = models.TextField()
    seniorityLevel = models.TextField()
    jobDescription = models.TextField()

    def __str__(self):
        return '''
        logo: {}
        Company Name: {}
        Job Title: {}
        Job Location: {}
        Employment Type: {}
        Seniority Level: {}
        Job Description: {}
        '''.format(self.logo, self.companyName, self.jobTitle, self.jobLocation,
                   self.employmentType, self.seniorityLevel,
                   self.jobDescription)

    @staticmethod
    def submit_job(logo, companyName, jobTitle, jobLocation, employmentType,
                   seniorityLevel, jobDescription):
        PostJob(
            logo=logo,
            companyName=companyName,
            jobTitle=jobTitle,
            jobLocation=jobLocation,
            employmentType=employmentType,
            seniorityLevel=seniorityLevel,
            jobDescription=jobDescription).save()

class Comment(models.Model):
    name = models.TextField()
    comment = models.TextField()
    post_comment = models.ForeignKey(PostJob, on_delete=models.PROTECT)
    post_comment = models.ForeignKey(PostJob, on_delete=models.CASCADE)

    def __str__(self):
        return '''
        Name: {}
        Comment: {}
        '''.format(self.name, self.comment, self.post_comment)

    @staticmethod
    def submit_comment(name, comment, post_comment_id):
        Comment(
            name=name, comment=comment,
            post_comment_id=post_comment_id).save()
