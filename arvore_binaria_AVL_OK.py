#Código desenvolvido por Thaynara Fumegali com o auxílio do ChatGPT

import random

class NoAVL: #Raiz inicial
    def __init__(self, valor):
        self.valor = valor      # Valores a serem armazenados na árvore 
        raiz = valor
        #chave
        self.esquerda = None
        self.direita = None
        self.altura = 1          # Valor inicial 
        #return raiz

class Arvore: 
    def __init__(self):
        self.raiz = None

    def altura (self, no):
        if no is None:
            return 0
        return no.altura
    
    def balanceamento(self, no): #fator_balanceamento
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)
    
    def atualiza_altura(self, no): #atualizar_altura
        if no is not None:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def f_direita(self, y): #rotacao_direita
        x = y.esquerda
        T2 = x.direita

        # Troca o lado
        x.direita = y
        y.esquerda = T2

        self.atualiza_altura(y)
        self.atualiza_altura(x)

        return x

    def f_esquerda(self, x): #rotacao_esquerda
        y = x.direita
        T2 = y.esquerda

        # Troca o lado
        y.esquerda = x
        x.direita = T2

        self.atualiza_altura(x)
        self.atualiza_altura(y)

        return y
    
    def inserir(self, raiz, valor):
        if raiz is None:
            raiz = valor
            return NoAVL(valor)
        
        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esqueda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)
        
        self.atualiza_altura(raiz) 

        bal = self.balanceamento(raiz)

        # Se desequilíbrio
        if bal > 1 and valor < raiz.esquerda.valor:
            return self.f_direita(raiz)
        
        if bal < -1 and valor > raiz.direita.valor: 
            return self.f_esquerda(raiz)
        
        if bal > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self.f_esquerda(raiz.esquerda)
            return self.f_direita(raiz)
        
        if bal < -1 and valor > raiz.direita.valor:
            raiz.direita = self.f_direita(raiz.direita)
            return self.f_esquerda(raiz)

        return raiz
    
    def remove(self, raiz, valor):
        if raiz is None:
            return raiz
        
        if valor < raiz.valor:
            raiz.esquerda = self.remove(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.remove(raiz.direita, valor)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self.min_no(raiz.direita) #minimo_valor_no
            raiz.valor = temp.valor
            raiz.direita = self.remove(raiz.direita, temp.valor)
        
        self.atualiza_altura(raiz)
        bal = self.balanceamento(raiz)

        # desequilíbrio
        if bal > 1 and self.balanceamento(raiz.esquerda) >= 0:
            return self.f_direita(raiz)
        
        if bal < -1 and self.balanceamento(raiz.direita) <= 0:
            return self.f_esquerda(raiz)
        
        if bal > 1 and self.balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.f_esquerda(raiz.esquerda)
            return self.f_direita(raiz)
        
        if bal < -1 and self.balanceamento(raiz.direita) > 0:
            raiz.direita = self.f_direita(raiz.direita)
            return self.f_esquerda(raiz)

        return raiz
    
    def min_no(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no
    
    def pesquisa(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        
        if valor < raiz.valor:
            return self.pesquisa(raiz.esquerda, valor)
        
        return self.pesquisa(raiz.direita, valor)
    
    def inserir_valor(self, valor):
        self.raiz = self.inserir(self.raiz, valor)

    def remover_valor(self, valor):
        self.raiz = self.remove(self.raiz, valor)

    def buscar_valor(self, valor):
        return self.pesquisa(self.raiz, valor)
    
    def buscar_valor2(self, valor):
        return self._buscar_valor2(self.raiz, valor)

    def _buscar_valor2(self, no, valor):
        if no is None:
            return None

        if valor == no.valor:
            return no.valor
        elif valor < no.valor:
            return self._buscar_valor2(no.esquerda, valor)
        else:
            return self._buscar_valor2(no.direita, valor)
        
    def conta_nos(self):
        global contador
        contador = 0

        def contar_nos_recursivo(no):
            global contador
            if no is not None:
                contador += 1
                contar_nos_recursivo(no.esquerda)
                contar_nos_recursivo(no.direita)

        contar_nos_recursivo(self.raiz)
        return contador
    
if __name__ == "__main__":
    print(u"\nExercicio 2 - Implementacao de arvores binarias AVL\n")
    teste = Arvore()
    i = 0
    while i <= 10:
        teste.inserir_valor(i)
        i += 1
    
    print("- Valores inseridos com sucesso.\nOs valores sao: ", )
    print("Tenho ", teste.conta_nos(), "nos")
    
    valores = []
    # tamanho = teste.conta_nos()
    # print(tamanho)
    a = 0
    while a < teste.conta_nos():
        valores.append(a+1)
        a += 1

    b = 0
    while b < teste.conta_nos():
        print(teste.buscar_valor2(b))
        b += 1
    
    #excluido = teste.remover_valor(random.choice(teste))
    teste.remover_valor(5) 
    if teste.buscar_valor2(5) == None:
        print("- Valor excluido com sucesso.")
    else:
        print("- Por algum motivo, nao consegui remover o numero solicitado, revise o codigo")
    
    busca = teste.buscar_valor2(2)
    print("- Procurei o valor: ", busca, "e encontrei!")