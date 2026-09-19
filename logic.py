from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Задание 2 - Импортируй нужные классы


class Question:
    def __init__(self, text, points, correct_index, *options):
        self.text = text          # обычное публичное поле
        self.points = points
        self.options = list(options)
        self.correct_index = correct_index

    @property
    def __text(self):
        return self.text

    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)
        buttons = []
        callback_data = 'correct'
        for i, option in enumerate(self.options):
            callback_data = 'correct' if i == self.correct_index else 'wrong'
            buttons.append(InlineKeyboardButton(option, callback_data=callback_data))

        markup.add(*buttons)  # добавляем все кнопки, row_width уже задан
        return markup


quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, 0, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, 1, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми"),
    Question("Кто проживает на дне океана?", 0, 0, "Спaнч-боб", "Гуф", "Глюкоза")
]
