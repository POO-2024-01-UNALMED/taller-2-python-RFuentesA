class Asiento:
    def __innit__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        ColoresValidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in ColoresValidos:
            self.color = color

class Auto:
    cantidadCreados = 0
    def __innit__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        asientos = self.asientos
        cantidad = 0
        for elementos in asientos:
            if isinstance(elementos, Asiento) == True:
                cantidad += 1
        return cantidad

    def verificarIntegridad(self):
        if (self.motor.registro == self.registro):
            for asiento in self.asientos:
                if (type(asiento) == Asiento):
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales" 


class Motor:
    def __innit__(self, numeroCilindros, tipo, registro): 
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == ("electrico" or "gasolina"):
            self.tipo = tipo
