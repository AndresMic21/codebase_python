import os

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment','host':'mongodb+srv://m220student:m220pwd1979@mflix.3souz.gcp.mongodb.net/UTA_Enrollment'}
