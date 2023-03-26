import os

os.system("git bisect start")
os.system("git bisect good e4cfc6f")
os.system("git bisect bad c1a4be0")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")
