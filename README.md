# Medical Reservations

###### Why are installed the package `python-stubs`?

This package help for some errors in my code editor: `Neovim`, for this reason the package are a complement for my LSP `Language Server Protocol` than I use `Basedpyright`.

###### What is that files?

Those files:

- `pyproject.toml`
- `pyrightconfig.json`

Those are some configurations for my code editor: `Neovim`, to use for autoformat `ruff` and LSP.

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
. venv/bin/activate # if use linux o mac
```

## Install packages 📦

```bash
pip install -r requirements.txt
```

### Superuser Credentials

```bash
python manage.py createsuperuser
```

- For generenal purpose

```bash
user -> admin
email -> admin@admin.com
pass -> admin
```

### Make migrations on Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

### Admin panel

`http://localhost:8000/admin/` and login with credential `superuser`, that we create early steps back.

### Dump Data

You choose, create manually all data information to try the app with admin panel, or dump the data app.

- Dump data:

```bash
python manage.py loaddata dump_medical_reservation.json
```

With this command, we get the mook data for try the app, you see the data with admin panel.

```bash
user -> admin
email -> admin@admin.com
pass -> admin
```

---

##### Create User for Doctors

Add new user, for example I create two users:
| Username | Password |
| -------------- | --------------- |
| DoctorHerrera | admin54321 |
| DoctorPerez | admin54321 |

> [!NOTE]
> Both users set `Staff Status`.

##### Create Specialtys

Go to the admin panel and create `Specialtys` for use then with `Doctors` relationships with DB.

##### Create Doctors

Go to the admin panel and create `Doctors`, the relationship with `Specialtys`

> [!NOTE]
> Dont Forget set `user` that we create early steps.

##### Create Patients

Go to the admin panel to create `Patients`.

##### Create Appointments

Go to the admin panel to create `Appointments`, that model are releated with `Doctor`, `Patients`.

## Why use admin panel instead api urls??

Well if you see the urls available, go to `http://localhost:8000` then you see something similar:

1. admin/
2. api/appointments/schedule/
3. api/
4. api/token/
5. api/token/refresh

> [!NOTE]
> The admin panel allows us to make CRUDS more faster, instead of using requests for the routes.

All routes are protected to have more security, if you able to go urls protected, you need to generate JWT Auth.

- With `POST` `http://localhost:8000/api/token/` - Body `Json`:

```json
{
  "username": "DoctorHerrera",
  "password": "admin54321"
}
```

Once you make the petition, we got 2 differents tokens:

- refresh
- access

### Try urls with JWT

> [!NOTE]
> Once you create `users`, `specialtys`, `doctors` and `appointments`.
> And generate JWT `access`.

Go to `GET` `http://127.0.0.1:8000/api/appointments/schedule/` with header `Authorization` `Bearer jwt_token_generated`

- This token was for `DoctorPerez` and get the appointments with this specific doctor

```json
[
  {
    "date": "2025-07-08T03:05:13Z",
    "appointments": [
      {
        "time": "03:05:14",
        "patient_name": "Erick"
      }
    ]
  },
  {
    "date": "2025-07-08T03:05:29Z",
    "appointments": [
      {
        "time": "03:05:30",
        "patient_name": "Kevin"
      }
    ]
  }
]
```

- Get the appointments for `DoctorHerrera`, before we need generate JWT

```json
[
  {
    "date": "2025-07-08T03:04:45Z",
    "appointments": [
      {
        "time": "03:04:49",
        "patient_name": "Kevin"
      }
    ]
  }
]
```
