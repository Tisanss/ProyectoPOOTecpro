import datetime
from abc import ABC, abstractmethod

# SRP: Clase solo representa el estado del sistema
class ArgenTour:
    def __init__(self, sistema_activo):
        self.sistema_activo = sistema_activo

class Servicio:
    def __init__(self, unidad, fecha_partida: datetime.datetime, fecha_llegada: datetime.datetime, calidad, precio, itinerario):
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio
        self.itinerario = itinerario

    def mostrar_infoservicio(self):
        return (
            f"{self.itinerario.mostrar_itinerario()}\n"
            f"Calidad: {self.calidad}, "
            f"Salida: {self.fecha_partida}, "
            f"Llegada: {self.fecha_llegada}, "
            f"Precio: ${self.precio}"
        )

    def mostrar_infoservicio_fecha(self, fecha_ini: datetime.datetime, fecha_fin: datetime.datetime):
        print(f"Patente de la unidad: {self.unidad.get_patente()}")
        if fecha_fin >= self.fecha_partida and fecha_ini <= self.fecha_llegada:
            print(
                f"{self.itinerario.mostrar_itinerario()}\n"
                f"Calidad: {self.calidad}, "
                f"Salida: {self.fecha_partida}, "
                f"Llegada: {self.fecha_llegada}, "
                f"Precio: ${self.precio}"
            )

class Pasajero:
    def __init__(self, nombre, email, dni):
        self.nombre = nombre
        self.email = email
        self.dni = dni

class Reserva:
    def __init__(self, pasajero, fecha_hora, asiento, servicio):
        self.pasajero = pasajero
        self.fecha_hora = fecha_hora
        self.asiento = asiento
        self.servicio = servicio
        self.pagada = False

    def mostrar_reserva(self):
        return (
            f"Reserva realizada: Pasajero {self.pasajero.nombre}, "
            f"Asiento {self.asiento.numero}, "
            f"Servicio del {self.servicio.fecha_partida.strftime('%d/%m/%Y %H:%M')}"
        )

    def caducar_reserva(self):
        tiempo_limite = self.servicio.fecha_partida - datetime.timedelta(minutes=30)
        if datetime.datetime.now() >= tiempo_limite and not self.pagada:
            self.asiento.ocupado = False
            print(f"[Reserva Caducada] La reserva de {self.pasajero.nombre} fue cancelada por falta de pago.")

class Unidad:
    def __init__(self, patente):
        self.patente = patente
        self.asientos = []
        for x in range(5):
            self.asientos.append(Asiento(x+1, False))

    def mostrar_asientos(self, ocupados=False):
        for a in self.asientos:
            if a.ocupado == ocupados:
                print(a.numero, end=", ")
        print()

    def get_patente(self):
        return self.patente

class Asiento:
    def __init__(self, numero, ocupado):
        self.numero = numero
        self.ocupado = ocupado

class Itinerario:
    def __init__(self, origen, destino, paradas=[]):
        self.origen = origen
        self.destino = destino
        self.paradas = paradas

    def mostrar_itinerario(self):
        paradas_str = ", ".join([p.nombre for p in self.paradas]) if self.paradas else "Sin paradas"
        return f"Origen: {self.origen.nombre}, Destino: {self.destino.nombre}, Paradas: {paradas_str}"

class Ciudad:
    def __init__(self, codigo, nombre, provincia):
        self.codigo = codigo
        self.nombre = nombre
        self.provincia = provincia

class MedioPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

    @abstractmethod
    def enviar_comprobante(self):
        pass

class MercadoPago(MedioPago):
    def __init__(self, celular, email):
        self.celular = celular
        self.email = email

    def procesar_pago(self, monto: float):
        def procesar_pago(self, monto : float ):
         print(f"[UALÁ] Enviando solicitud de pago de ${monto:.2f} " )
         
         transaccion_id = f"UA-{int(datetime.datetime.now().timestamp())}"
         print(f"Código de pago generado: {transaccion_id[-6:]}")
         print("Esperando confirmación del usuario...")
         print("Pago recibido exitosamente.")

    def enviar_comprobante(self):
        comprobante = (
             f"[MERCADO PAGO] Enviando comprobante al correo {self.email}...\n"
             f"----- COMPROBANTE DE PAGO -----\n"
             f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
             f"Cuenta asociada: {self.celular}\n"
             f"-------------------------------\n"
         )
        print(comprobante)

class Uala(MedioPago):
    def __init__(self, email, nombre_titular):
         self.email = email
         self.nombre_titular = nombre_titular

    def procesar_pago(self, monto : float ):
         print(f"[UALÁ] Enviando solicitud de pago de ${monto:.2f} " )
         
         transaccion_id = f"UA-{int(datetime.datetime.now().timestamp())}"
         print(f"Código de pago generado: {transaccion_id[-6:]}")
         print("Esperando confirmación del usuario...")
         print("Pago recibido exitosamente.")
    
    def enviar_comprobante(self):
        comprobante = (
            f"[UALÁ] Enviando comprobante al correo {self.email}...\n"
            f"----- COMPROBANTE DE PAGO -----\n"
            f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
            f"Usuario asociado: {self.nombre_titular}\n"
            f"-------------------------------\n"
        )
        print(comprobante) 

class TarjetaCredito(MedioPago):
    def __init__(self, numero, DNITitular, nombre, fecha_vencimiento):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.numero =numero
        self.DNITitular =DNITitular
    
    def procesar_pago(self, monto : float ):
         print(f"Procesando pago de ${monto:.2f} con tarjeta de crédito.")
         
         if(self.fecha_vencimiento > datetime.datetime.today()):
             print(f"Pago autorizado por ${monto:.2f}.")
         else:
             print("Error: Pago no autorizado. La tarjeta esta vencida")

    def enviar_comprobante(self):  
        if(self.fecha_vencimiento > datetime.datetime.today()):
            ultimos_digitos = str(self.numero)[-4:]
            comprobante = (
             f"COMPROBANTE DE PAGO\n"
             f"---------------------\n"
             f"Tarjeta: **** **** **** {ultimos_digitos}\n"
             f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
             f"Usuario Asociado: {self.nombre}, DNI: {self.DNITitular}"
             f"Comprobante enviado al HomeBanking asociado a esta tarjeta.\n"
            )
            print(comprobante)
         
    
        
class Venta:
    def __init__(self, medio_pago: MedioPago, monto, reserva: Reserva, fecha_hora):
        self.medio = medio_pago
        self.monto = monto
        self.reserva = reserva
        self.fecha_hora = fecha_hora

    def cobrar(self):
        self.medio.procesar_pago(self.monto)
        self.reserva.pagada = True
        self.medio.enviar_comprobante()

    def get_monto(self):
        return self.monto
    def get_metodo(self):
        return self.medio.__class__.__name__

class Informe:
    def init(self,servicios:list[Servicio],ventas:list[Venta],fecha_desde:datetime.date, fecha_hasta:datetime.date):
        self.desde=fecha_desde
        self.hasta=fecha_hasta
        self.servicios:list[Servicio]=servicios
        self.ventas:list[Venta]=ventas
        self.total_faccturado=0
        self.canti_ventas=0

    def mostrar_informe(self):
        for serv in self.servicios:
            serv.mostrar_infoservicio_fecha(self.desde, self.hasta)
        print("Detalle de pagos:")
        for pag in self.ventas:
            self.canti_ventas += 1
            self.total_faccturado += pag.get_monto()
            print(f"Monto pagado: {pag.get_monto()} con {pag.get_metodo()}")
        print(f"Monto total de {self.canti_ventas} pagos: {self.total_faccturado}")

if __name__ == "__main__":
    argentour1 = ArgenTour(True)

    pasajero1 = Pasajero("Martin Perez", "martinelmascrack777@gmail.com", 36566999)
    ciudad_origen = Ciudad("1000", "Buenos Aires", "Buenos Aires")
    ciudad_destino = Ciudad("3100", "Paraná", "Entre Ríos")
    ciudad_parada = Ciudad("3000", "Santa Fe", "Santa Fe")

    itinerario1 = Itinerario(ciudad_origen, ciudad_destino, [ciudad_parada])
    itinerario2 = Itinerario(ciudad_origen, ciudad_destino, [ciudad_parada])
    itinerario3 = Itinerario(ciudad_origen, ciudad_destino, [ciudad_parada])
    unidad1 = Unidad("123 ABC")
    unidad2 = Unidad("456 EFG")
    unidad3 = Unidad("789 HIJ")

    servicio1 = Servicio(unidad1, datetime.datetime(2025, 5, 6, 10, 0), datetime.datetime(2025, 5, 6, 18, 0), "Ejecutivo", 50000, itinerario1)
    servicio2 = Servicio(unidad2, datetime.datetime(2025, 8, 5, 11, 0), datetime.datetime(2025, 9, 6, 18, 0), "Turista", 30000, itinerario1)
    servicio3 = Servicio(unidad3, datetime.datetime(2025, 11, 9, 12, 0), datetime.datetime(2025, 12, 6, 18, 0), "Ejecutivo", 60000, itinerario1)
    servicios = [servicio1,servicio2,servicio3]

    uala1 = Uala("martinelmascrack777@gmail.com","Martin Perez")
    mercadopago1 = MercadoPago(3435557777,"email@gmail.com")
    tarjetacredito1 = TarjetaCredito(2505541254125632, 44777555, "Nombre", 2026)

    ventas = []

    print("Servicios disponibles:")
    for i, s in enumerate(servicios, 1):
        print(f"Servicio {i}:")
        print(s.mostrar_infoservicio())

    servicio_seleccionado = int(input("¿Qué servicio desea seleccionar? ")) - 1
    servicio = servicios[servicio_seleccionado]

    print("Asientos disponibles: ", end="")
    servicio.unidad.mostrar_asientos(False)

    asiento_seleccionado = int(input("¿Qué asiento desea reservar? ")) - 1
    if 0 <= asiento_seleccionado < len(servicio.unidad.asientos) and not servicio.unidad.asientos[asiento_seleccionado].ocupado:
        servicio.unidad.asientos[asiento_seleccionado].ocupado = True
        asiento = servicio.unidad.asientos[asiento_seleccionado]
        reserva = Reserva(pasajero1, datetime.datetime.now(), asiento, servicio)
        print(reserva.mostrar_reserva())

        # Preguntar si se paga la reserva
        pagar = input("¿Desea pagar ahora? (y/n): ").lower()
        if pagar == 'y':
            print("===¿Qué metodo de pago desea seleccionar?=== \n==>1: Mercado Pago \n==>2: Ualá \n==>3: Tarjeta de credito\n")
            opcion = int(input())

            metodo = None
            match opcion:
                case 1:
                    metodo = mercadopago1
                case 2:
                    metodo = uala1
                case 3:
                    metodo = tarjetacredito1
                case _:
                    print("Opción inválida")

            total_a_abonar = servicios[servicio_seleccionado].precio
            metodo.procesar_pago(total_a_abonar)
            venta1=Venta(metodo,total_a_abonar,total_a_abonar,datetime.datetime.today())
            metodo.enviar_comprobante()

            ventas.append(venta1)
        else:
            print("No se pagó la reserva aún. Se mantendrá hasta 30 minutos antes de la salida.")


        # Simular vencimiento:
        reserva.caducar_reserva()
    else:
        print("Asiento no disponible.")

    # Mensaje despues de haber hecho la reserva
    print("Asientos libres: ", end="")
    servicios[servicio_seleccionado].unidad.mostrar_asientos(False)
    print("/ Ocupados: ", end="")
    servicios[servicio_seleccionado].unidad.mostrar_asientos(True)
    
    r_info_usuario=input("Mostrar informe de servicios?(y/n):")

    if r_info_usuario =='y':
        print("Mostrando datos:")
           
        informe_loc=Informe(servicios,ventas,datetime.date(2020,1,1),datetime.date(2025,12,31))
        informe_loc.mostrar_informe()
    
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

