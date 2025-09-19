# 📬 Servidor de Correo en Python

Este proyecto implementa un sistema básico de servidor de correo electrónico utilizando **programación orientada a objetos (POO)** en Python. Se modelan las entidades principales de un sistema de mensajería: usuarios, mensajes, carpetas y el servidor de correo. El sistema aplica principios como **encapsulamiento**, **interfaces**, y diseño modular.

---

## 🧱 Estructura del Proyecto

### Clases Principales

- **Usuario**: Representa a un usuario del sistema. Puede enviar y recibir mensajes, y organizar su correo en carpetas.
- **Mensaje**: Contiene información del mensaje como remitente, destinatario, asunto, contenido y fecha.
- **Carpeta**: Agrupa mensajes bajo un nombre específico (ej. “inbox”, “enviados”). Permite listar y almacenar mensajes.
- **ServidorCorreo**: Administra el registro de usuarios y su acceso.

### Interfaces (Abstract Base Classes)

- **IEnviar**: Define el comportamiento para enviar mensajes.
- **IRecibir**: Define el comportamiento para recibir mensajes.
- **IListarMensajes**: Define el comportamiento para listar mensajes.

---