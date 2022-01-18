class CuentaBancaria:
    
    def __init__(self, tasa_interes, balance=0): 
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito(self, amount):
        self.balance += amount 
        print("Deposito realizado correctamente.")
        return self

    def retiro(self, amount):
        if self.balance < amount:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            if self.balance >= 5: self.balance -= 5             
        else:
            self.balance -= amount 
            print("Retiro realizado correctamente.")
        return self

    def mostrar_info_cuenta(self):
        print("Balance:",self.balance, "- Tasa de interés:", self.tasa_interes)
        return self

    def generar_interés(self):
        if CuentaBancaria.balancePositivo(self.balance):
            self.balance += (self.balance*self.tasa_interes)
        return self
    
    @staticmethod
    def balancePositivo(balance):
        if balance>0: return True
        else: return False
    
    
       
