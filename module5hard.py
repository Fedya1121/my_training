import hashlib
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age
        self.adult_mode = False


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode




class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname not in self.users:
            raise ValueError("Пользователь не найден")
        user = self.users[nickname]
        if hashlib.sha256(password.encode()).hexdigest():
            self.current_user = user
        else:
            raise ValueError("Неверный пароль")

    def register(self, nickname, password, age):
        if nickname in self.users:
            raise ValueError(f"Пользователь {nickname} уже существует")
        self.users[nickname] = User(nickname, password, age)

    def log_out(self):
        if not self.current_user:
            raise ValueError("Пользователь не авторизован")
        print(f"Пользователь {self.current_user.nickname} вышел из системы.")
        self.current_user = None

    def add(self, title, duration, adult_mode=False):
        video = Video(title, duration, adult_mode)
        self.videos.append(video)

    def get_videos(self, title):
        return [video.title for video in self.videos if title.lower() in video.title.lower()]

    def watch_video(self, title):
        user = self.current_user
        if not user:
            raise ValueError("Войдите в аккаунт, чтобы смотреть видео")

        for video in self.videos:
            if video.title.lower() == title.lower():
                if not user.adult_mode and user.age < 18 and video.adult_mode:
                    raise ValueError("Вам нет 18 лет, пожалуйста покиньте страницу")

                for second in range(1, 11):
                    print(f"{second}")
                    sleep(1)

                print("Конец видео")
                return

        raise ValueError("Видео не найдено.")






if __name__ == "__main__":
    ur = UrTube()
    ur.add('Лучший язык программирования 2024 года', 200)
    ur.add('Для чего девушкам парень программист?', 10, adult_mode=True)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)

    try:
        ur.watch_video('Для чего девушкам парень программист?')
    except ValueError as e:
        print(e)

    ur.log_in('vasya_pupkin', 'lolkekcheburek')

    try:
        ur.watch_video('Для чего девушкам парень программист?')
    except ValueError as e:
        print(e)


    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')

    try:
        ur.watch_video('Для чего девушкам парень программист?')
    except ValueError as e:
        print(e)

    try:
        ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    except ValueError as e:
        print(e)

    try:
        ur.watch_video('Лучший язык программирования 2024 года!')
    except ValueError as e:
        print(e)










