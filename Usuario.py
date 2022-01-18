from CuentaBancaria import CuentaBancaria

class Usuario:

    def __init__(self, nombre, apellido, balanceInicial=0):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = CuentaBancaria(0.04, balanceInicial)
        self.cuentas = []
        self.cuentas.append(self.cuenta)
    
    def hacer_retiro(self, amount):
        if self.cuenta.balance < amount:
            print("No cuenta con el saldo suficiente para realizar la operación.")
        else:
            self.cuenta.retiro(amount)
        return self

    def hacer_deposito(self, amount):
        self.cuenta.deposito(amount) 
        return self

    def mostrar_info_usuario(self):
        print("Usuario:", self.nombre, self.apellido, end=" - ")
        self.cuenta.mostrar_info_cuenta()
        return self

    def transfer_dinero(self, other_user, amount):
        if self.cuenta.balance < amount:
            print("No cuenta con el saldo suficiente para realizar la operación.")
        else:
            other_user.cuenta.balance += amount
            self.cuenta.balance -=amount
            print("Tranferencia realizada.")
        return self

    def crearNuevaCuenta(self, balance=0):       
        self.cuentas.append(CuentaBancaria(0.04, balance))
    
    def muestraCuentas(self):
        print("Tienes", len(self.cuentas), "cuenta(s) con nosotros, aquí el detalle:")
        for i in self.cuentas:
            i.mostrar_info_cuenta()
