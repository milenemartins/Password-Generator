import random

def generate_password(favorite_animal, series_movie_anime, date, favorite_month):
    # Tratamento de erros para garantir que as entradas não estejam vazias
    if not favorite_animal or not series_movie_anime or not date or not favorite_month:
        raise ValueError("Todos os campos devem ser preenchidos.")

    password = ''

    # Adicionando parte do animal favorito à senha
    password += favorite_animal[:2].lower()

    # Adicionando parte da série/filme/anime à senha
    password += series_movie_anime[:2].lower()

    # Adicionando parte da data à senha
    password += date[-2:]

    # Adicionando parte do mês favorito à senha
    password += favorite_month[:2].lower()

    # Escolhendo um caractere especial aleatoriamente
    special_character = random.choice('!@#$%&')

    # Calculando o número de caracteres aleatórios necessários para alcançar uma senha de 8 caracteres
    num_random_characters = max(0, 8 - len(password))

    # Adicionando caracteres aleatórios
    available_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    password += ''.join(random.choices(available_characters, k=num_random_characters))

    # Adicionando o caractere especial
    password += special_character

    return password[:8]  # Truncando a senha para 8 caracteres, se necessário

def main():
    try:
        favorite_animal = input("Digite um animal que você goste: ")
        series_movie_anime = input("Digite uma série, filme ou anime: ")
        date = input("Digite uma data no formato (DD/MM/AAAA): ")
        favorite_month = input("Digite um mês favorito: ")

        password = generate_password(favorite_animal, series_movie_anime, date, favorite_month)
        print("A senha gerada é:", password)
    except ValueError as ve:
        print("Erro:", ve)

if __name__ == "__main__":
    main()
