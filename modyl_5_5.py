class User:
    users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        User.users.append(self)

    @classmethod
    def find_user(cls, nickname):
        for user in cls.users:
            if user.nickname == nickname:
                return user
        return None


class Video:
    videos = []

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        Video.videos.append(self)

    @classmethod
    def find_video(cls, title):
        for video in cls.videos:
            if video.title.lower() == title.lower():
                return video
        return None


class UrTube:
    def __init__(self):
        self.current_user = None

    def log_in(self, nickname, password):
        user = User.find_user(nickname)
        if user and user.password == password:
            print(f"Добро пожаловать, {user.nickname}")
            self.current_user = user
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        if User.find_user(nickname):
            print(f"Пользователь с ником {nickname} уже существует.")
        else:
            user = User(nickname, password, age)
            self.current_user = user
            print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("Нет пользователя, вошедшего в систему.")

    def add_video(self, *videos):
        for video in videos:
            if isinstance(video, Video):
                print(f"Видео '{video.title}' добавлено на платформу.")
            else:
                print("Объект не является видео.")

    def get_videos(self, search_term):
        found_videos = [video.title for video in Video.videos if search_term.lower() in video.title.lower()]
        if found_videos:
            print(f"Найденные видео: {found_videos}")
        else:
            print("Видео не найдены.")

    def watch_video(self, video_title):
        if self.current_user:
            video = Video.find_video(video_title)
            if video:
                if video.adult_mode and self.current_user.age < 18:
                    print(f"Контент {video.title} доступен только для взрослых.")
                else:
                    print(f"Начинаем просмотр: {video.title}")
                    print(f"Продолжительность видео: {video.duration} секунд.")
            else:
                print(f"Видео с названием '{video_title}' не найдено.")
        else:
            print("Сначала войдите в систему, чтобы смотреть видео.")


ur_tube = UrTube()

ur_tube.register('vasya_pupkin', 'lolkekcheburek', 13)
ur_tube.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur_tube.add_video(v1, v2)

ur_tube.get_videos('лучший')
ur_tube.get_videos('ПРОГ')

ur_tube.watch_video('Для чего девушкам парень программист?')
ur_tube.log_in('vasya_pupkin', 'lolkekcheburek')
ur_tube.watch_video('Для чего девушкам парень программист?')

ur_tube.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur_tube.watch_video('Для чего девушкам парень программист?')





  
