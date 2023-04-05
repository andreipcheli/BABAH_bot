from spotify.main import get_response_from_spotify, check_response_from_spotify
from genius.main import get_response_from_genius, check_response_from_genius

def get_song_name():
    pass


def create_response(data):
    unvalid_spotify = get_response_from_spotify(data)
    valid_spotify = check_response_from_spotify(unvalid_spotify)


def main():
    # Отправить сообщение
    # Получить название трека (get_song_name())
    # Отправить в create_response
    # Отправить сообщение из create_response
    data = get_song_name()
    create_response(data)


if __name__ == '__main__':
    main()