import os 

def exibir_nome_do_programa(): 
   print("""
░██████╗░██████╗░██╗██╗░░░░░██╗░░░░░  ███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██████╗░
██╔════╝░██╔══██╗██║██║░░░░░██║░░░░░  ██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██╔══██╗
██║░░██╗░██████╔╝██║██║░░░░░██║░░░░░  █████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██████╔╝
██║░░╚██╗██╔══██╗██║██║░░░░░██║░░░░░  ██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██╔══██╗
╚██████╔╝██║░░██║██║███████╗███████╗  ██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. listar restaurante")
    print("3. ativar restaurante")
    print("4. sair\n ")

def finalizar_app() :
   os.system('cls')
   print('finalizando app \n')


def escolher_opcao(): 
    opcao = int(input("digite a opção desejada: "))


    if opcao == 1: 
        print('cadastrar restaurante')
    elif opcao == 2: 
        print('listar restaurante')
    elif opcao == 3: 
        print('ativar restaurante')
    else:  
        finalizar_app()
    
 
def main(): 
     exibir_nome_do_programa()
     exibir_opcoes()
     escolher_opcao()
     
if __name__ == '__main__': 
     main()