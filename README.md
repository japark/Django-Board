# Django-Board
Realization of board, tag, and login/logout/signup with Django Framework


After git clone, follow these:

1) Enter the "Django-Board" directory.

2) Make virtual environment:
   - virtualenv venv
   - venv\Scripts\activate (Or "source venv/bin/activate" in Mac)
   - pip install -r requirements.txt

3) python manage.py migrate

4) python manage.py createsuperuser
   - Fill in username, email address, password, password(again).

5) python manage.py runserver
   - Go to 127.0.0.1:8000/admin
   - Login with superuser account made above.
   - You can now control the admin site.

6) Go to 127.0.0.1:8000
   - It's the "Django-Board" website, which is intented to show you.
