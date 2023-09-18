from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0):
        self.agencia = agencia
        self.numero_conta = numero_conta,
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        print(
            f'R$ {valor:.2f} depositado na sua conta. \
            \nSaldo atual: R$ {self.saldo:.2f}')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        limite = -self.limite
        if self.saldo - valor >= limite:
            self.saldo -= valor
            print(f'R$ {valor:.2f} sacado. \
                   Saldo atualizado: R$ {self.saldo:.2f}')
            return self.saldo
        print(
            f'Saldo insuficiente: R$ {self.saldo:.2f}; \
            Limite: R$ {-self.limite:.2f}')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numero_conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 0):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor: float) -> float:
        if self.saldo - valor >= 0:
            self.saldo -= valor
            print(f'R$ {valor:.2f}. Saldo atualizado: R$ {self.saldo:.2f}')
            return self.saldo
        print(f'Saldo insuficiente: R$ {self.saldo:.2f}')
        return self.saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 100)
    cp1.sacar(1)
    cp1.depositar(5)
    cp1.sacar(3)
    print('####')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(5)
    cc1.sacar(110)
