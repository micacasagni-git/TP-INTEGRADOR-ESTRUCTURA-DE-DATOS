class Usuario:
    
    def __init__(self, nombre, apellido, correo_electronico, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.__contrasena = contrasena

    def crear_mensaje(self):
        pass

    def cambiar_contraseña(self):
        pass

    def filtrar_mensajes(self):
        pass

    def abrir_mensaje(self):
        pass

    def eliminar_mensaje(self):
        pass
    
    def marcar_leido(self):
        pass
