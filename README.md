# 🧠 Clean Architecture in Django

> A practical example of how to apply **Clean Architecture** principles in a Django application — from Domain and UseCases to Infrastructure and Interface layers.
>
> 🎥 Watch the full video explanation here → [**YouTube Video**](https://youtu.be/1AJGWgFDNYk)
> 💻 Explore the code on GitHub → [**Repository**](https://github.com/https://github.com/ndongchrist/django-clean-architecture)

---

## 🚀 Overview

This project demonstrates how to build a **clean, scalable, and maintainable** Django application using **Clean Architecture** principles.

The main goal is to **separate business logic from frameworks and tools**, making your codebase:

* Easier to test 🧪
* Easier to maintain 🛠️
* Easier to scale ⚙️

---

## 🧩 Architecture Overview

The project is organized into **four main layers**:

### 1. **Domain**

> The core of your business logic — pure Python code, no dependencies.
> This layer defines **entities**, **interfaces**, and **rules**.

### 2. **Application (UseCases)**

> Contains your **application logic** — how the system behaves.
> Orchestrates the interaction between the domain and other layers.

### 3. **Infrastructure**

> Handles all external concerns like database, APIs, email, etc.
> In Django, this is where you’ll typically find models, repositories, or adapters.

### 4. **Interface (Presentation Layer)**

> The layer that communicates with the outside world — Django views, REST APIs, GraphQL, CLI, etc.

---

## 🧱 Folder Structure Example

```
.
├── domain/
│   ├── entities/
│   ├── repositories/
│   └── services/
│
├── application/
│   ├── usecases/
│   └── interfaces/
│
├── infrastructure/
│   ├── orm/
│   ├── repositories/
│   └── configurations/
│
├── interface/
│   ├── api/
│   ├── web/
│   └── cli/
│
├── manage.py
└── requirements.txt
```

---

## 💡 Why Clean Architecture?

* 🔹 **Independent from frameworks** – Django becomes just a tool, not a constraint.
* 🔹 **Easier testing** – You can test business rules without touching the database or API.
* 🔹 **Flexible structure** – Switch frameworks, databases, or UIs without breaking your core logic.
* 🔹 **Long-term scalability** – Your project stays clean and maintainable as it grows.

---

## 🧠 Principles Behind It

This architecture is built around the **SOLID principles**:

* **S**ingle Responsibility
* **O**pen/Closed
* **L**iskov Substitution
* **I**nterface Segregation
* **D**ependency Inversion

These principles help keep each component focused, modular, and reusable.

---

## ⚙️ Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/django-clean-architecture.git
   cd django-clean-architecture
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and start the server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Open your browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## 🧑‍💻 About This Project

This repository is a practical guide for developers who want to **structure Django projects the right way** — using clean architecture principles inspired by **Robert C. Martin (Uncle Bob)**.

If you want to learn how to separate business logic, make your code testable, and think like a software architect — this is for you.
