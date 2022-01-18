from codecs import utf_16_be_decode

from Usuario import Usuario


u1 = Usuario("Victor", "Vasquez")
u2 = Usuario("Susan", "Espino")
u3 = Usuario("Jashury", "Chavez", 500)

u1.hacer_deposito(200)
u2.hacer_deposito(150)
u3.hacer_retiro(100)

u1.transfer_dinero(u3, 50)

u1.mostrar_info_usuario()
u2.mostrar_info_usuario()
u3.mostrar_info_usuario()

u1.muestraCuentas()
u1.crearNuevaCuenta(5000)
u1.muestraCuentas()


u1.hacer_retiro(50)
u1.mostrar_info_usuario()

