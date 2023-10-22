# Кожухов Сергей, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# Функция для позитивной проверки

def positive_assert(order_body):
    # В переменную kit_response сохраняется результат запроса на создание пользователя
    sender_stand_request.post_new_order(order_body)
    order_of_track = sender_stand_request.get_order_of_track(sender_stand_request.track)
    # Проверяется, что код ответа равен 200
    assert order_of_track.status_code == 200
    #print(order_of_track.status_code)


#тест №1 на провреку статуса запроса на получение заказа по его номеру
def test1_create_order():
    order_body = data.order_body
    positive_assert(order_body)
