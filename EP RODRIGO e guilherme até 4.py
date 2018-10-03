# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 12:13:37 2018

@author: rodri
"""
import json
with open ('Arquivo.txt','r') as arquivo:
    info = arquivo.read()
    cardapio = json.loads(info)

comanda = {}

#abrindo o arquivo


#HUB de escolhas
print("Comanda eletrônica")
print("0 - sair",
      "1 - imprimir cardápio",
      "2 - adicionar item à comanda",
      "3 - remover item",
      "4 - imprimir comanda",
      "5 - Adicionar produto ao cardápio",
      "6 - Remover produto do cardápio",
      "7 - Adicionar uma nova comanda")

escolha = int(input("Faça sua escolha: "))



while escolha > 0: 
       
#Adicionar produtos
    
    if escolha == 1:
            print('O cardápio possui os seguintes itens:')
            for produto in cardapio:
                print(
                      '{0}:'.format(produto), '{0} R$'.format(cardapio[produto]))
    
    if escolha == 2 :
        produto= input("Escreva o nome do produto desejado:")
        produto = produto.lower()
        if produto not in cardapio:
            print('O produto não está no cardápio')
            break
        quantidade = int(input('Digite a quantidade do produto: '))
        if quantidade < 0:
            print('A quantidade tem de ser positiva e inteira')
            break
      
       
        
        
        comanda[produto] = {}
        comanda[produto]= quantidade
       # for produto in comanda:
         #   print('{0}:'.format(produto), '{0} R$'.format(comanda[produto]))
    
    if escolha == 3 :
        produto= input("Escreva o nome do produto que deseja tirar da comanda:")
        produto = produto.lower()
        if produto not in comanda:
            print('O produto não está na comanda')
            break
        if produto in comanda:
            quantidade = int(input('Digite quanto do produto deseja remover:'))
            if quantidade > 0:
                comanda[produto] -= quantidade
                if comanda[produto] <= 0:
                    del comanda[produto]
                    print('Produto removido da comanda')
            if quantidade < 0 :
                print('Não se pode remover uma quantidade negativa')
                break
            
        
             
    if escolha == 4:
        lista_preco_tot=[]
        for produto in comanda:
            preco_unitario = float(cardapio[produto])
            quantidade_produto = int(comanda[produto])
            preco_tot =  preco_unitario * quantidade_produto
            lista_preco_tot.append(preco_tot)
            
            print('{0}:'.format(produto),"{0}".format(comanda[produto]))
            print('Preço Unitário {0} R$'.format(preco_unitario))
            print('Preço Total {0} R$'.format(preco_tot))
            total_final= sum(lista_preco_tot,0)
            total_final10 = 1.1 * total_final
            
           
        
        print('Preço final sem 10%: {0:.2f} R$'.format(total_final))
        print('Preço final com 10%: {0:.2f} R$'.format(total_final10))
            
        
        
            
    if escolha == 6:
        produto = input('Digite o nome do produto que deseja remover: ')
        produto = produto.lower()
        if produto not in cardapio:
            print('O produto não está no cardápio')
            break
        else:
            del cardapio[produto]
            
    if escolha == 5:
        produto = input('Digite o nome do produto que deseja adicionar: ')
        produto = produto.lower()
        if produto in cardapio:
            print('O produto já está no cardápio')
            break
        else:
            preco= float(input('Digite o preço do produto:'))
            cardapio[produto] = preco
            if preco < 0: 
                print('O preço não pode ser negativo')
        
        
    
            
        
        
       
        
        
       


#volta ao HUB

    
    print("Comanda eletrônica")
    print("0 - sair",
      "1 - imprimir cardápio",
      "2 - adicionar item à comanda",
      "3 - remover item",
      "4 - imprimir comanda",
      "5 - Adicionar produto ao cardápio",
      "6 - Remover produto do cardápio",
      "7 - Adicionar comanda")

    escolha = int(input("Faça sua escolha: "))
    
  
    
#Encerra o programa

if escolha == 0:
    print("até mais!")



with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(cardapio, sort_keys=True, indent=4)
    arquivo.write(conteudo)

    
    

