import datetime 
from abc import ABC, abstractmethod

#SRP: Clase solo representa el estado del sistema


class Venta:
    def __init__(self, fecha_hora):
        self.fecha_hora = fecha_hora

class Pasajero:
    def __init__(self, nombre, email, dni):
        self.nombre = nombre
        self.email = email
        self.dni = dni
        
class Reserva:
    def __init__(self, pasajero, fecha_hora, asiento):
        self.pasajero = pasajero
        self.fecha_hora = fecha_hora
        self.asiento = asiento

class Unidad:
    def __init__(self, patente):
        self.patente = patente

class Asiento:
    def __init__(self, numero, ocupado):
        self.numero = numero 
        self.ocupado = ocupado

class Itinerario:
    def __init__(self, origen, destino, paradas:list):
        self.origen = origen
        self.destino = destino
        self.paradas = paradas #Es una lista de ciudad (de los objetos), puede tener varias paradas antes de llegar al destino

    def mostrar_itinerario(self):
        if self.paradas and len(self.paradas) > 0:
            nombres_paradas = []
            for parada in self.paradas:
                nombres_paradas.append(nombres_paradas)
            paradas_str = ", ".join(nombres_paradas) #es una linea de strings que separa las paradas con una ","
        else:
            paradas_str = "Sin paradas"
        origen_str = f"Origen: {self.origen.nombre}"
        destino_str = f"Destino: {self.origen.destino}"
        resultado = f"{origen_str}, {destino_str}, Paradas: {paradas_str}"
        return resultado
    

class Ciudad:
    def __init__(self, codigo, nombre, provincia):
        self.codigo = codigo
        self.nombre = nombre 
        self.provincia = provincia
#Una interfez, X metodos, redefine, los usan las clases hijas
class MedioPago (ABC):
    @abstractmethod   
    def __init__(self):
        pass
    def procesar_pago(self, monto):
        pass

class MercadoPago(MedioPago):
    def __init__(self, celular, email):
        super().__init__()
        self.celular = celular
        self.email = email
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)

class Uala(MedioPago):
    def __init__(self, email, nombre_titular):
        super().__init__()
        self.email = email
        self.nombre_titular = nombre_titular
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)    

class TarjetaCredito(MedioPago):
    def __init__(self, numero, DNITitular, nombre, fecha_vencimiento):
        super().__init__()
        self.numero = numero
        self.DNITitular = DNITitular
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)
    
class Servicio:
    def __init__(self, unidad: Unidad, fecha_partida:datetime.date, fecha_llegada:datetime.date, calidad, precio):
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio
    def mostrar_infoservicio(self):
        print(f"Unidad: {self.unidad}\n")
        print(f"Fecha partida: {self.fecha_partida}\n")
        print(f"Fecha llegada: {self.fecha_llegada}\n")
        print(f"Calidad: {self.calidad}\n")
        print(f"Precio: {self.precio}\n")
    
class ArgenTour:
    def __init__(self, sistema_activo):
        self.sistema_activo = sistema_activo
        
   

if __name__ == "__main__":

    argentour1 = ArgenTour(True)
    venta1 = Venta(datetime.time(14,30,00))
    unidad1 = Unidad("123 ABC")
    pasajero1 = Pasajero("Martin","martinelmascrack777@gmail.com",36566999)
    asiento1 = Asiento(44,True)
    reserva1 = Reserva(pasajero1,datetime.time(15,45,00),asiento1)
    
    #falta declarar itinerario
    ciudad1 = Ciudad("3100","Parana","Entre rios")
    #falta declarar medio_pago
    mercadopago1 = MercadoPago("44542631","pedritopepito@gmail.com")
    tarjetacredito1 = TarjetaCredito("84545231",44843333,"Juancito",datetime.date(2025,10,10))
    servicio1 = Servicio(unidad1,datetime.date(2025,5,6),datetime.date(2025,6,3),"Premium",50000)
    #lista de servicios 

    #Para cada servicio en la lista de servicios ordenada le corresponde un itinerario en la 
    # lista de itinerarios ordenada las cuales se muestran como sigue
    servicios:list[Servicio]=[]
    itinerarios:list[Itinerario]=[]
    servicios.append(servicio1)
    serv_cont=1
    for serv,iti in zip(servicios, itinerarios):
        print("Información del servicio  {serv_cont}\n")
        serv.mostrar_infoservicio()
        iti.mostrar_itinerario()
        

#para hacer un commit:
# guardalo
# abri tu ruta de carpeta en el cmd
# git add Sistema.py
# git commit -m "mensaje aclarando q hiciste"
# git push        

#para guardar un commit:
# git stash
# git pull
# git stash pop 
        