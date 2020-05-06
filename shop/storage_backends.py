from abc import ABC

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage, ABC):
    bucket_name = 'starshop25'
    location = 'media'
    file_overwrite = False


class StaticStorage(S3Boto3Storage, ABC):
    bucket_name = 'starshop25'
    location = 'static'
    file_overwrite = False
