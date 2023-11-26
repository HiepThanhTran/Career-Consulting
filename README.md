# BlueCC - Blue Career Consult

BlueCC is a project using Django Framework of our group in the Information System Security subject

## Installation
1. Clone the project:

```bash
git clone https://github.com/HiepThanhTran/BlueCC.git
```

2. Open project on Pycharm and install dependencies from requirements.txt

- Open terminal and cd to the directory containing the manage.py file:

Example:
```bash
-Your directory
 --BlueCC
   ---BlueCC
   ---....
   ---manage.py
```
- And run:
```bash
pip install -r requirements.txt
```

3. Makemigration and migrate database:
```bash
python manage.py makemigrations
python manage.py migrate
```

*Note*: Make sure you connect to your database configured in the settings.py file:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.<ENGINE>',
        'NAME': '<DATABASE_NAME>',
        'USER': '<DATABASE_USER>',
        'PASSWORD': 'DATABASE_PASSWORD>',
        'HOST': '<YOUR HOST>',
        'PORT': '<YOUR PORT>'
    }
}
```

*Or you can use sqlite3:
```bash
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     },
}
```

## Usage
- After that just run project:

HTTP Protocol
```bash
python manage.py runserver
```

HTTPS Protocol (For Login/Signup with Facebook)
```bash
python manage.py runsslserver
```
