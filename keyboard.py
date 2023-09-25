from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add(KeyboardButtonType.text('Каталог'),
          KeyboardButtonType.text('Корзина'),
          KeyboardButtonType.text('Контакты'))

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add(KeyboardButtonType.text('Каталог'),
                KeyboardButtonType.text('Корзина'),
                KeyboardButtonType.text('Контакты'),
                KeyboardButtonType.text('Админ-панель'))

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add(KeyboardButtonType.text('Добавить товар'),
                KeyboardButtonType.text('Удалить товар'),
                KeyboardButtonType.text('Сделать рассылку'))

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', callback_data='t-shirt'),
                 InlineKeyboardButton(text='Шорты', callback_data='shorts'),
                 InlineKeyboardButton(text='Кроссовки', callback_data='sneakers'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add(KeyboardButtonType.text('Отмена'))