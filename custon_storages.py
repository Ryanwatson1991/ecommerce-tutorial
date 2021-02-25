from django.conf import settings
from storages.backends.s3boto import s3Boto3Storage


class StaticStorage(s3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(s3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

