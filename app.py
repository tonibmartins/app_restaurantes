import os

restaurants = [{"nome" : "Praça", "categoria" : "Japonesa", "ativo" : False},{"nome" : "Pizza Suprema", "categoria" : "Italiana", "ativo" : True}, {"nome" : "Bulls", "categoria" : "Hamburgueria", "ativo" : False}]

def show_name_program():
    print("""
      
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      """)

def show_op():
    print("1 - Cadastrar Restaurante")
    print("2 - Listar Restaurante")
    print("3 - Alterar Status do Restaurante")
    print("4 - Sair do Sistema\n")

def op_error():
    print("Opção inválida, tente novamente!\n")
    main_return()

def main_return():
    input("Pressione qualquer tecla e confirme para continuar... \n")
    main()

def status_restaurant():
    show_subtitles("Alterando Status do restaurante\n")

    restaurant_name = input("Digite o nome do restaurante: \n\n")

    restaurant_find = False

    for restaurant in restaurants:
        if restaurant_name == restaurant["nome"] :
            restaurant["ativo"] = not restaurant["ativo"]
            restaurant_find = True
            print(f"Status do restaurante {restaurant_name} alterado com sucesso!\n")
    if not restaurant_find:
        print(f"Restaurante {restaurant_name} não encontrado!\n")

            
def select_op():
    try:
        op_select = int(input("Escolha uma opção: "))
        if op_select == 1:
            new_restaurant()
        elif op_select == 2:
            list_restaurants()
        elif op_select == 3:
            status_restaurant()
        elif op_select == 4:
            close_program()
        else:
            op_error()
    except:
        op_error()

def close_program():
    show_subtitles("Finalizando o programa...")

def new_restaurant():   
    show_subtitles("Cadastro de Restaurante\n")

    restaurant_name = input("Digite o nome do restaurante: \n\n")

    category = input(f"Digite a categoria do restaurante {restaurant_name} : \n\n")

    restaurant_data = {"nome" : restaurant_name, "categoria" : category, "ativo" : False}

    restaurants.append(restaurant_data)

    print(f"\nRestaurante {restaurant_name} foi cadastrado com sucesso!\n")

    main_return()

def list_restaurants():
    show_subtitles("Listagem de Restaurantes")

    print(f"{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}\n")

    for restaurant in restaurants:
        restaurant_name = restaurant["nome"]
        restaurant_category = restaurant["categoria"]
        restaurant_status = "Ativo" if restaurant["ativo"] else "Inativo"
        print(f" - {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_status}\n")

    main_return()

def show_subtitles(texto):
    os.system('cls')
    line = "=" * len(texto)
    print(line)
    print(texto)
    print(line)

def main():
    os.system('cls')
    show_name_program()
    show_op()
    select_op()

if __name__ == "__main__":
    main()





