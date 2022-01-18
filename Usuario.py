import random
from CuentaBancaria import CuentaBancaria

class Usuario:

    def __init__(self, nombre, apellido, balanceInicial=0):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = CuentaBancaria(0.04, balanceInicial)
        self.cuentas = {}
        anID = Usuario.createID()
        self.cuentas[anID] = self.cuenta
        print ("Bienvenido", self.nombre, "se te ha creado una cuenta con ID:", anID)
    
    def hacer_retiro(self, amount):
        id=int(input("Ingrese el ID de la cuenta a retirar:"))
        if id in self.cuentas:
            if self.cuentas[id].balance < amount:
                print("No cuenta con el saldo suficiente para realizar la operación.")
            else:
                self.cuentas[id].retiro(amount) 
        else: 
            print("Error, no se ha encontrado el ID.")    

        return self

    def hacer_deposito(self, amount):
        id=int(input("Ingrese el ID de la cuenta a depositar:"))
        if id in self.cuentas:
            self.cuentas[id].deposito(amount) 
        else: 
            print("Error, no se ha encontrado el ID.")
        return self

    def mostrar_info_usuario(self):
        print("Usuario:", self.nombre, self.apellido)
        print("CUENTAS:")
        for key in self.cuentas:
            print("ID", key, ": Balance:", self.cuentas[key].balance)           
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
        self.nuevaCuenta = CuentaBancaria(0.04, balance)
        anID = Usuario.createID()
        self.cuentas[anID] = self.nuevaCuenta
        print ("Hola", self.nombre, "se te ha creado una nueva cuenta con ID:", anID)       
        
    """
    def muestraCuentas(self):
        print("Tienes", len(self.cuentas), "cuenta(s) con nosotros, aquí el detalle:")
        for i in self.cuentas:
            i.mostrar_info_cuenta()
    """
    
    @staticmethod
    def createID():
        return random.randint(50000, 80000)
        
