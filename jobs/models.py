from django.db import models

class JobOffer(models.Model):
    available = models.BooleanField(default=True)
    DEVELOPER = 'DEV'
    QUALITY_ANALYST = 'QA'
    BUSINESS_ANALYST = 'BA'
    EXPERIENCE_DESIGNER = 'XD'
    JOB_TITLE_CHOICES = [
        (DEVELOPER, 'Developer'),
        (QUALITY_ANALYST, 'Quality Analyst'),
        (BUSINESS_ANALYST, 'Business Analyst'),
        (EXPERIENCE_DESIGNER, 'Experience Designer')
    ]
    
    job_title = models.CharField(max_length=3, choices=JOB_TITLE_CHOICES, default=DEVELOPER)
    job_description = models.TextField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    company_name = models.CharField(max_length=10)
    company_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.job_title} by {self.company_name}'