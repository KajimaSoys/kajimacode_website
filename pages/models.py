from django.db import models


language_choices = (
    ('ru', 'Русский'),
    ('en', 'Английский')
)


class Navbar(models.Model):
    """
    Описание модели Navbar приложения Pages
    """

    class Meta:
        verbose_name = 'Навигационная панель'
        verbose_name_plural = 'Навигационные панели'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    projects_link = models.CharField(verbose_name='Проекты', max_length=60)
    skills_link = models.CharField(verbose_name='Скиллы', max_length=60)
    about_link = models.CharField(verbose_name='Обо мне', max_length=60)
    telegram_button = models.CharField(verbose_name='Кнопка связаться', max_length=60)

    def __str__(self):
        return f'Navbar - {self.language}'


class Footer(models.Model):
    """
    Описание модели Footer приложения Pages
    """

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    overview_link = models.CharField(verbose_name=f'Обзор', max_length=60)
    projects_link = models.CharField(verbose_name=f'Проекты', max_length=60)
    skills_link = models.CharField(verbose_name=f'Скиллы', max_length=60)
    about_link = models.CharField(verbose_name=f'Обо мне', max_length=60)
    terms_link = models.CharField(verbose_name=f'Условия', max_length=60)
    privacy_link = models.CharField(verbose_name=f'Конфиденциальность', max_length=60)
    cookies_link = models.CharField(verbose_name=f'Cookies', max_length=60)

    def __str__(self):
        return f'Footer - {self.language}'


class CookieElement(models.Model):
    """
    Описание модели Cookie приложения Pages
    """

    class Meta:
        verbose_name = 'Всплывающее окно cookie'
        verbose_name_plural = 'Всплывающие окна cookie'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    element_text = models.CharField(verbose_name='Текст', max_length=60)
    link = models.CharField(verbose_name='Ссылка', max_length=60)
    button = models.CharField(verbose_name='Кнопка', max_length=60)

    def __str__(self):
        return f'Cookie - {self.language}'


class RateElement(models.Model):
    """
    Описание модели Rate приложения Pages
    """

    class Meta:
        verbose_name = 'Модуль обратной связи'
        verbose_name_plural = 'Модули обратной связи'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    # rate section
    rate_title = models.CharField(verbose_name='Заголовок оценки', max_length=50, blank=True)
    rate_title_success = models.CharField(verbose_name='Заголовок оценки в случае отправки', max_length=50, blank=True)

    feedback_title = models.CharField(verbose_name='Заголовок фидбека', max_length=150, blank=True)
    feedback_description = models.CharField(verbose_name='Описание фидбека', max_length=300, blank=True)

    feedback_message_label = models.CharField(verbose_name='Лейбл сообщения', max_length=50, blank=True)
    feedback_message_placeholder = models.CharField(verbose_name='Плейсхолдер сообщения', max_length=50, blank=True)

    feedback_success_message = models.CharField(verbose_name='Сообщение об успехе', max_length=60, blank=True)
    feedback_error_message = models.CharField(verbose_name='Сообщение об ошибке', max_length=60, blank=True)

    send_button = models.CharField(verbose_name='Кнопка отправки', max_length=60, blank=True)
    send_button_wait = models.CharField(verbose_name='Кнопка отправки - ожидание', max_length=60, blank=True)
    retry_button = models.CharField(verbose_name='Повторить', max_length=60, blank=True)

    def __str__(self):
        return f'Rate - {self.language}'


class MainPage(models.Model):
    """
    Описание модели Main приложения Pages
    """
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    # buttons
    contact_button = models.CharField(verbose_name='Свяжитесь со мной', max_length=50)
    projects_button = models.CharField(verbose_name='Проекты', max_length=50)
    get_started_button = models.CharField(verbose_name='Начните', max_length=50)
    learn_more_button = models.CharField(verbose_name='Узнать больше', max_length=50)
    send_message_button = models.CharField(verbose_name='Отправить заявку', max_length=50)
    send_message_button_wait = models.CharField(verbose_name='Кнопка отправки - ожидание', max_length=60, blank=True)
    retry_button = models.CharField(verbose_name='Повторить', max_length=60, blank=True)

    # main section
    main_title = models.CharField(verbose_name='Заголовок главной секции', max_length=150)

    # introduce section
    introduce_title = models.CharField(verbose_name='Заголовок секции вступления', max_length=150)
    introduce_description = models.CharField(verbose_name='Описание секции вступления', max_length=1000)

    # project section
    project_title = models.CharField(verbose_name='Заголовок секции проектов', max_length=150)
    project_description = models.CharField(verbose_name='Описание секции проектов', max_length=1000)

    # stages section
    stages_title = models.CharField(verbose_name='Заголовок секции стадий разработки', max_length=150)

    discussion_title = models.CharField(verbose_name='Заголовок обсуждения', max_length=50)
    discussion_description = models.CharField(verbose_name='Описание обсуждения', max_length=1000)

    concept_title = models.CharField(verbose_name='Заголовок концепта', max_length=50)
    concept_description = models.CharField(verbose_name='Описание концепта', max_length=1000)

    server_dev_title = models.CharField(verbose_name='Заголовок разработки сервера и бд', max_length=50)
    server_dev_description = models.CharField(verbose_name='Описание разработки сервера и бд', max_length=1000)

    ui_dev_title = models.CharField(verbose_name='Заголовок разработки UI', max_length=50)
    ui_dev_description = models.CharField(verbose_name='Описание разработки UI', max_length=1000)

    test_title = models.CharField(verbose_name='Заголовок тестирования', max_length=50)
    test_description = models.CharField(verbose_name='Описание тестирования', max_length=1000)

    deploy_title = models.CharField(verbose_name='Заголовок деплоя', max_length=50)
    deploy_description = models.CharField(verbose_name='Описание деплоя', max_length=1000)

    first_string = models.CharField(verbose_name='Первая часть слогана', max_length=50)
    second_string = models.CharField(verbose_name='Вторая часть слогана-ссылка', max_length=50)
    third_string = models.CharField(verbose_name='Третья часть слогана', max_length=50)

    # technologies section
    technologies_title = models.CharField(verbose_name='Заголовок секции используемых технологий', max_length=150)

    django_title = models.CharField(verbose_name='Заголовок сервера', max_length=50)
    django_description = models.CharField(verbose_name='Описание сервера', max_length=1000)

    postgresql_title = models.CharField(verbose_name='Заголовок БД', max_length=50)
    postgresql_description = models.CharField(verbose_name='Описание БД', max_length=1000)

    vue_title = models.CharField(verbose_name='Заголовок фронта', max_length=50)
    vue_description = models.CharField(verbose_name='Описание фронта', max_length=1000)

    # contact section
    contact_pretitle = models.CharField(verbose_name='Предзаголовок секции связи', max_length=50)
    contact_title = models.CharField(verbose_name='Заголовок секции связи', max_length=150)
    contact_description = models.CharField(verbose_name='Описание секции связи', max_length=300)

    name_label = models.CharField(verbose_name='Лейбл имени', max_length=50)
    name_placeholder = models.CharField(verbose_name='Плейсхолдер имени', max_length=50)

    email_label = models.CharField(verbose_name='Лейбл емайла', max_length=50)
    email_placeholder = models.CharField(verbose_name='Плейсхолдер емайла', max_length=50)

    message_label = models.CharField(verbose_name='Лейбл сообщения', max_length=50)
    message_placeholder = models.CharField(verbose_name='Плейсхолдер сообщения', max_length=50)

    privacy_text = models.CharField(verbose_name='Сообщение согласия', max_length=50)
    privacy_link = models.CharField(verbose_name='Сообщение-ссылка на условия', max_length=50)

    success_message = models.CharField(verbose_name='Сообщение об успехе', max_length=60, blank=True)
    error_message = models.CharField(verbose_name='Сообщение об ошибке', max_length=60, blank=True)

    # review section
    review_title = models.CharField(verbose_name='Заголовок секции отзывов', max_length=150)
    review_description = models.CharField(verbose_name='Описание секции отзывов', max_length=300)

    first_text = models.CharField(verbose_name='Текст певрого отзыва', max_length=50)
    first_author = models.CharField(verbose_name='Автор певрого отзыва', max_length=50)
    first_post = models.CharField(verbose_name='Должность певрого автора', max_length=50)

    second_text = models.CharField(verbose_name='Текст второго отзыва', max_length=50)
    second_author = models.CharField(verbose_name='Автор второго отзыва', max_length=50)
    second_post = models.CharField(verbose_name='Должность второго автора', max_length=50)

    third_text = models.CharField(verbose_name='Текст третьего отзыва', max_length=50)
    third_author = models.CharField(verbose_name='Автор третьего отзыва', max_length=50)
    third_post = models.CharField(verbose_name='Должность третьего автора', max_length=50)

    def __str__(self):
        return f'Main - {self.language}'


class ProjectsPage(models.Model):
    """
    Описание модели Projects приложения Pages
    """
    class Meta:
        verbose_name = 'Страница проектов'
        verbose_name_plural = 'Страницы проектов'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    back_button = models.CharField(verbose_name='Назад', max_length=50)

    def __str__(self):
        return f'Projects - {self.language}'


class SkillsPage(models.Model):
    """
    Описание модели Skills приложения Pages
    """
    class Meta:
        verbose_name = 'Страница скиллов'
        verbose_name_plural = 'Страницы скиллов'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    title = models.CharField(verbose_name='Заголовок', max_length=40)

    backend_title = models.CharField(verbose_name='backend - заголовок', max_length=20, blank=True)
    backend_description = models.TextField(verbose_name='backend - описание', blank=True)

    frontend_title = models.CharField(verbose_name='frontend - заголовок', max_length=20, blank=True)
    frontend_description = models.TextField(verbose_name='frontend - описание', blank=True)

    other_title = models.CharField(verbose_name='Другое - заголовок', max_length=20, blank=True)
    other_description = models.TextField(verbose_name='Другое - описание', blank=True)

    def __str__(self):
        return f'Skills - {self.language}'


class AboutPage(models.Model):
    """
    Описание модели About приложения Pages
    """
    class Meta:
        verbose_name = 'Страница о себе'
        verbose_name_plural = 'Страницы о себе'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    title = models.CharField(verbose_name='Заголовок', max_length=40)
    about_text = models.TextField(verbose_name='Текст о себе')

    resume_text = models.CharField(verbose_name='Заголовок для блока резюме', max_length=60)
    download_button = models.CharField(verbose_name='Кнопка для скачивания', max_length=40)

    def __str__(self):
        return f'About - {self.language}'


class TermsPage(models.Model):
    """
    Описание модели Terms приложения Pages
    """
    class Meta:
        verbose_name = 'Страница с условиями'
        verbose_name_plural = 'Страницы с условиями'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    data = models.TextField(verbose_name='Политика', max_length=100000, blank=True)

    def __str__(self):
        return f'Terms - {self.language}'


class PrivacyPage(models.Model):
    """
    Описание модели Privacy приложения Pages
    """
    class Meta:
        verbose_name = 'Страница с Конфиденциальностью'
        verbose_name_plural = 'Страницы с Конфиденциальностью'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    data = models.TextField(verbose_name='Политика', max_length=100000, blank=True)

    def __str__(self):
        return f'Privacy - {self.language}'


class CookiesPage(models.Model):
    """
    Описание модели Cookies приложения Pages
    """
    class Meta:
        verbose_name = 'Страница с cookies'
        verbose_name_plural = 'Страницы с cookies'

    language = models.CharField(verbose_name='Язык', max_length=6, choices=language_choices, default='en')

    data = models.TextField(verbose_name='Политика', max_length=100000, blank=True)

    def __str__(self):
        return f'Cookies - {self.language}'

