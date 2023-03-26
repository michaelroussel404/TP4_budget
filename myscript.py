import os

os.system("git bisect start e4cfc6f c1a4be0")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
