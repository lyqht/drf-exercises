from rest_framework import serializers
from jobs.models import JobOffer

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        exclude = ['id']