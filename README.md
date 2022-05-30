# Social Network

REST API for a social network made with Django, DRF and their fantastic features. Includes token authentication (JWT). Handling posts and comments using the security measures and permissions implementation provided by DRF. Fast and secure.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/social-network.git
```

Then, in the project directory, you install the requirements.

```
pip install -r requirements.txt
```

Now, make the migrations.

```
python3 manage.py migrate
```

And finally, run the project.

```
python3 manage.py runserver
```

Ready, now your API is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source ven/bin/activate
```