import random

def generate_password_prefixes(favorite_animal, series_movie_anime, date, favorite_month):
    return (
        favorite_animal[:2].lower(),
        series_movie_anime[:2].lower(),
        date[-2:],
        favorite_month[:2].lower()
    )

def generate_random_characters(length):
    available_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choices(available_characters, k=length))

def generate_password(favorite_animal, series_movie_anime, date, favorite_month):
    if not all((favorite_animal, series_movie_anime, date, favorite_month)):
        raise ValueError("Todos os campos devem ser preenchidos.")

    prefix1, prefix2, date_suffix, month_prefix = generate_password_prefixes(favorite_animal, series_movie_anime, date, favorite_month)
    special_character = random.choice('!@#$%&')
    random_characters_length = max(0, 8 - len(prefix1 + prefix2 + date_suffix + month_prefix))

    password = prefix1 + prefix2 + date_suffix + month_prefix
    password += generate_random_characters(random_characters_length)
    password += special_character

    return password[:8]

def main():
    try:
        password = generate_password()
        print("A senha gerada é:", password)
    except ValueError as ve:
        print("Erro:", ve)

if __name__ == "__main__":
    main()
