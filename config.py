import os

root = os.path.abspath(os.path.dirname(__name__))

#
# CONFIG
#
DATABASE = os.path.join(root, "datastore.db")


DEBUG = True
SECRET_KEY = "I am the snow man!"

USERNAME = "xcubic"
PASSWORD = "11111"
