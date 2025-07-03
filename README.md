# Django Blog Platform

> A simple and functional blogging platform built with Django.  
> Plataforma de blogging simple y funcional desarrollada con Django.

---

## 🌐 English Version

### Overview

This is a multi-user blog application where registered users can publish their own posts, manage their profiles, and interact with the platform through a personal dashboard. Staff users (admins) have extended permissions to manage all content and users.

### Features

- **User authentication**: Registration, login, logout, password change.
- **User profiles**: Edit personal information and avatar.
- **Post management**: Authenticated users can create, edit, and delete their own posts.
- **Admin dashboard**: Staff users can manage all posts and registered users.
- **Public homepage**: Unauthenticated users can browse recent posts.

### Tech Stack

- Python 3
- Django
- SQLite
- Bootstrap (via CDN)

### Installation

```bash
git clone https://github.com/facupetri/django-blog-app
cd django-blog-app
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access the application at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Project Structure

- `base/` – Main blog functionality (views, templates).
- `users/` – User management and authentication.
- `media/` – Uploaded images (avatars, post images).
- `static/` – Static files (CSS, JS).
- `config/` – Core settings and project configuration.

### Demo

▶️ [Watch video demo](https://www.loom.com/share/7c1ccd2fabe04a43869bf0a190eb58e8?sid=7b6891c9-8656-4f90-ada2-146886fb22a4)

---

## 🇪🇸 Versión en Español

### Descripción

Aplicación web de blog multiusuario. Los usuarios registrados pueden publicar, editar y eliminar sus propios posts, así como gestionar su perfil personal. Los administradores tienen acceso a un panel especial con permisos para gestionar todos los contenidos y usuarios.

### Características

- **Autenticación de usuarios**: Registro, inicio de sesión, cierre de sesión, cambio de contraseña.
- **Perfiles de usuario**: Edición de información personal y avatar.
- **Gestión de publicaciones**: Crear, editar y eliminar posts propios.
- **Panel de administración**: Los administradores pueden gestionar todos los posts y usuarios.
- **Página pública**: Los visitantes no registrados pueden ver publicaciones recientes.

### Tecnologías utilizadas

- Python 3
- Django
- SQLite
- Bootstrap (desde CDN)

### Instalación

```bash
git clone https://github.com/facupetri/django-blog-app
cd django-blog-app
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accedé a la app en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Estructura del proyecto

- `base/` – Funcionalidad principal del blog (vistas, templates).
- `users/` – Manejo de usuarios y autenticación.
- `media/` – Imágenes subidas (avatares, imágenes de publicaciones).
- `static/` – Archivos estáticos (CSS, JS).
- `config/` – Configuración y núcleo del proyecto.

### Demo

▶️ [Ver demostración en video](https://www.loom.com/share/7c1ccd2fabe04a43869bf0a190eb58e8?sid=7b6891c9-8656-4f90-ada2-146886fb22a4)

---

### 👤 Autor

Facundo Petringa  
[GitHub](https://github.com/facupetri) · [LinkedIn](https://www.linkedin.com/in/facupetri/)
