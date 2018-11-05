from obj_reader import file_obj


def main():
    while(1):
        file_name = input('Nome do arquivo .OBJ: ')

        file = file_obj(file_name)
        file.leitura_obj()

        file_write = input('Nome do arquivo de escrita .OBJ: ')
        file.escreve_obj(file_write)

        next = input("Deseja ler outro arquivo? S/N  ")
        if next == 'N':
            break
        elif next == 'S':
            pass
        else:
            print('Entrada inválida')



if __name__ == '__main__':
    main()


arquivo = file_obj
