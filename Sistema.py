import datetime 
from abc import ABC, abstractmethod

#SRP: Clase solo representa el estado del sistema
class ArgenTour:
    def __init__(self, sistema_activo):
        self.sistema_activo = sistema_activo  

class Servicio:
    def __init__(self, unidad, fecha_partida:datetime.date, fecha_llegada:datetime.date, calidad, precio, itinerario):
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio
        self.itinerario = itinerario
    def mostrar_infoservicio(self):
        return{
            f"{self.itinerario.mostrar_itinerario()}\n"
            f"Calidad: {self.calidad}, "
            f"Salida: {self.fecha_partida},"
            f"Llegada: {self.fecha_llegada},"
            f"Precio: ${self.precio}"
        }


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
        self.asientos = []
        for x in range(5):
            self.asientos.append(Asiento(x+1,False)) #x+1 para que la lista de asientos no arranque de 0 (muero croto)
            
    def mostrar_asientos(self):
        for a in self.asientos:
            print(a.numero," ")
            
        
        

class Asiento:
    def __init__(self, numero, ocupado):
        self.numero = numero 
        self.ocupado = ocupado

class Itinerario:
    def __init__(self, origen, destino, paradas = []):
        self.origen = origen
        self.destino = destino
        self.paradas = paradas #Es una lista de ciudad (de los objetos), puede tener varias paradas antes de llegar al destino

    def mostrar_itinerario(self):
        if self.paradas and len(self.paradas) > 0:
            nombres_paradas = []
            for parada in self.paradas:
                nombres_paradas.append(parada.nombre)
            paradas_str = ", ".join(nombres_paradas) #es una linea de strings que separa las paradas con una ","
        else:
            paradas_str = "Sin paradas"
        origen_str = f"Origen: {self.origen.nombre}"
        destino_str = f"Destino: {self.destino.nombre}"
        resultado = f"{origen_str}, {destino_str}, Paradas: {paradas_str}"
        return resultado
    

class Ciudad:
    def __init__(self, codigo, nombre, provincia):
        self.codigo = codigo
        self.nombre = nombre 
        self.provincia = provincia
        
        
#Una interfez, X metodos, redefine, los usan las clases hijas
class MedioPago (ABC):
    #Clase interfaz no lleva init (en ese caso definiria comportamiento en una clase abstracta)
    
    @abstractmethod   
    def procesar_pago(self, monto : int): #procesa el pago acorde a cada metodo simulado
        pass
    
    @abstractmethod
    def enviar_comprobante(self): #deja registro de la operacion, debe incluir datos de pasajero y del asiento 
        pass
    
    #se pueden seguir agregando metodos abstractos, siempre y cuando los usen todos los servicios. Los servicios no deberian tener metodos que no esten especificados en esta interfaz
     
#"Las ventas implican la validación de un medio de pago a traves de un servicio externo simulado". Simulamos el servicio de cada uno? o lo dejamos abstracto?
class MercadoPago(MedioPago):
    def __init__(self, celular, email):
        self.celular = celular
        self.email = email
        
    def procesar_pago(self, monto):
        ...
    
    def enviar_comprobante(self):
        ...

class Uala(MedioPago):
    def __init__(self, email, nombre_titular):
        self.email = email
        self.nombre_titular = nombre_titular
        
    def procesar_pago(self, monto):
        ...
    
    def enviar_comprobante(self):
        ...    

class TarjetaCredito(MedioPago):
    def __init__(self, numero, DNITitular, nombre, fecha_vencimiento):
        self.numero = numero
        self.DNITitular = DNITitular
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
    
    def procesar_pago(self, monto):
        ...
    
    def enviar_comprobante(self): #enviarlo a la pagina del banco? que el usuario lo vea en homebanking 
        ...
    

if __name__ == "__main__":

    argentour1 = ArgenTour(True)
    venta1 = Venta(datetime.time(14,30,00))
    
    pasajero1 = Pasajero("Martin","martinelmascrack777@gmail.com",36566999)
    reserva1 = Reserva(pasajero1,datetime.time(15,45,00),44)
    asiento1 = Asiento(44,True)
    #falta declarar itinerario
    ciudad1 = Ciudad("3100","Parana","Entre rios")
    #falta declarar medio_pago
    mercadopago1 = MercadoPago("44542631","pedritopepito@gmail.com")
    tarjetacredito1 = TarjetaCredito("84545231",44843333,"Juancito",datetime.date(2025,10,10))

    ciudad_origen = Ciudad("1000","Buenos Aires","Buenos Aires")
    ciudad_destino = Ciudad("3100", "Paraná", "Entre Ríos")
    ciudad_parada = Ciudad("3000","Santa Fe","Santa Fe")

    itinerario1 = Itinerario(ciudad_origen,ciudad_destino, [ciudad_parada])
    unidad1 = Unidad("123 ABC")
    servicio1 = Servicio(unidad1,datetime.date(2025,5,6),datetime.date(2025,6,3),"Premium",50000,itinerario1)
    servicio2 = Servicio(unidad1, datetime.date(2025,5,10),datetime.date(2025,5,11),"Comun",40000,itinerario1)
    servicios = [servicio1, servicio2]
    
    print("Servicios disponibles: ")
    counter = 1
    for s in servicios:
        print("Servicio ",counter,":")
        print(s.mostrar_infoservicio())
        counter+= 1
        
    servicio_seleccionado = int(input("¿Qué servicio desea seleccionar?")) 
    print("Asientos disponibles: [")
    servicios[servicio_seleccionado].unidad.mostrar_asientos()
    print("]")
    
    
    
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
        