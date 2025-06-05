# 📝 Django Task Manager API

A simple RESTful Task Manager API built with Django and Django REST Framework.

## 🚀 Features

* ✅ Create, list, update, and delete tasks
* 📆 RESTful endpoints using `ModelViewSet`
* 🌐 Beautiful landing page
* 🧪 Built-in browsable API for testing in browser
* 🔐 CORS enabled for frontend integration

---

## ⚙️ Endpoints

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| GET    | `/api/tasks/`     | List all tasks        |
| POST   | `/api/tasks/`     | Create a new task     |
| PUT    | `/api/tasks/:id/` | Mark task as complete |
| DELETE | `/api/tasks/:id/` | Delete a task         |

You can test the API directly in your browser thanks to Django REST Framework's browsable interface.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/beimnetmelese/kuraz-intership.git
   cd KurazTech
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Visit the homepage**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📁 Project Structure

```
KurazTask/
│
├── Task/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── templates/
│       └── your_app/
│           └── home.html
│
├── KurazTask/
│   └── settings.py
│
├── requirements.txt
└── manage.py
```

---

## 🤩 Tech Stack

* Python 3.12+
* Django
* Django REST Framework
* django-cors-headers

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
