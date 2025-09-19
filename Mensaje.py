class Mensaje:
    def __init__(self, texto, archivos_adjuntos, destinatario, remitente, asunto):
        self.__texto = texto
        self.__archivos_adjuntos = archivos_adjuntos
        self.__estado = "pendiente"
        self.__destinatario = destinatario
        self.__remitente = remitente
        self.__asunto = asunto

    def editar_mensaje(self):
        pass

    def enviar_mensaje(self):
        pass
    
    def adjuntar_archivos(self):
        pass

    def responder_mensaje(self):
        pass

    def reenviar_mensaje(self):
        pass

