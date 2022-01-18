#La opcion de elegir cuentas solo se puede aplicar para retiros y depositos, más no para tranferencias, ya que el ejercicio 
#se volvería más complejo y tomaría más de lo requerido

from Usuario import Usuario

u1 = Usuario("Victor", "Vasquez")
u2 = Usuario("Susan", "Espino")
u3 = Usuario("Jashury", "Chavez", 500)

u1.hacer_deposito(200)

u1.crearNuevaCuenta(5000)
u1.hacer_retiro(2500)
u1.mostrar_info_usuario()
u1.hacer_retiro(1000)

