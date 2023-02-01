class User():

    def __init__(self, id, nombre=None, apellido=None, rut=None, cargo=None, descripcion=None, pais=None, ciudad=None, postal=None, celular=None, correo=None) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.cargo = cargo
        self.descripcion = descripcion
        self.pais = pais
        self.ciudad = ciudad
        self.postal = postal
        self.celular = celular
        self.correo = correo

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'rut': self.rut,
            'cargo': self.cargo,
            'descripcion': self.descripcion,
            'pais': self.pais,
            'ciudad': self.ciudad,
            'postal': self.postal,
            'celular': self.celular,
            'correo': self.correo
        }

