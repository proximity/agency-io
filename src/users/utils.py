import os

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ext = filename.split('.')[-1]
    return 'employee/{0}-{1}-{2}.{3}'.format(instance.id, instance.first_name, instance.last_name, ext)
