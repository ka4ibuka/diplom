import configuration
import requests
import data

#создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  #URL+ручка для создания заказа
                         json=body)  #заголовки

response = post_new_order(data.order_body);

track = response.json()["track"] #получение track созданного пользователя
#print(track)

#получение заказа
def get_order_of_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.NUMBER_ORDER+str(track))  #URL+ручка для получения заказа по номеру
#response = get_order_of_track (track);

#status_track = response.status_code #получение статуса заказа
#print(status_track)


