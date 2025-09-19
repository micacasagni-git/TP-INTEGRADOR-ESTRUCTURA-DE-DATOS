# 📬 Servidor de Correo en Python
---

## 🧱 Estructura del Proyecto

### Clases Principales

- **Usuario**: Representa a un usuario del sistema. Puede enviar y recibir mensajes, y organizar su correo en carpetas.
- **Mensaje**: Contiene información del mensaje como remitente, destinatario, asunto, contenido y fecha.
- **Carpeta**: Agrupa mensajes bajo un nombre específico (ej. “inbox”, “enviados”). Permite listar y almacenar mensajes.
- **ServidorCorreo**: Administra el registro de usuarios y su acceso.


### Diagrama de clases
<!-- Diagrama SVG -->
<p align="center">
  <img src="./assets/diagrama.svg">
</p>


### Interfaces (Abstract Base Classes)

- **IEnviar**: Define el comportamiento para enviar mensajes.
- **IRecibir**: Define el comportamiento para recibir mensajes.
- **IListarMensajes**: Define el comportamiento para listar mensajes.

---