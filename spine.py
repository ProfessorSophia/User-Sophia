import os


# O objetivo deste script é fazer com que o diretório 'C:\Users\35193\Downloads' seja limpo, usando um parser. 

Download_Path = r"C:\Users\35193\Downloads"

# Função para listar ficheiros numa pasta
def listar_ficheiros(pasta):
    try:
        # Obtém a lista de ficheiros na pasta
        ficheiros = os.listdir(pasta)
        
        # Filtra apenas os ficheiros (exclui diretórios)
        ficheiros = [f for f in ficheiros if os.path.isfile(os.path.join(pasta, f))]
        print(ficheiros[1:-1])
        print(ficheiros)
        print(type(ficheiros))

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
listar_ficheiros(Download_Path)


