import requests

__secret_key__ = "AQVN38CDRBlod2wbgEbrgemiKeDC8BZ88Ni_o3-1"
__storage_id__ = "b1gjtlqofdt5mu5io6a9"
__url__ = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'


__system_promt__ = ('Ты главный редактор делового СМИ в Татарстане. '
                    'Определи от 0 до 10 важность этого события для публикации в твоем СМИ, '
                    'которое посвящено только Татарстану. '
                    'Если новости НЕ ОТНОСИТСЯ К ТАТАРСТАНУ, то ставь оценку 2. '
                    'Если это анонс любого мероприятия, то ставь оценку 2. '
                    'Если это новость про событие, произошедшее в деревне, то ставь оценку 2. '
                    'В твоем СМИ пишут только наиболее важные общественные новости, а также новости, посвященные '
                    'бизнесу, экономике и финансам. В твоем СМИ НЕ ПИШУТ ПРО АНОНСЫ МЕРОПРИЯТИЙ, ТЕАТРАЛЬНЫЕ '
                    'ПРЕДСТАВЛЕНИЯ, КОНЦЕРТЫ, ФЕСТИВАЛИ, ВЫСТАВКИ, ДОНОРОВ КРОВИ, КРИПТОВАЛЮТУ, ВОЙНУ, '
                    'ВРУЧЕНИЕ ПОДАРКОВ КОМУ УГОДНО, ФРАНШИЗЫ, про кульутрыне мероприятия '
                    'в школах или детских садах. В твоем СМИ не пишут про мелкие события '
                    'в районах Татарстана. Если в новости уоминается «ПЖКХ», УК «ПЖКХ», то ставь оценку 2. '
                    'В ответ пришли только число')

__headers__ = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {}".format(__secret_key__)
}


temp = 0


# Functions for admin
def admin_set_system_promt(system_promt_text=__system_promt__):
    global __system_promt__
    __system_promt__ = str(system_promt_text)


def admin_set_temp(new_temp) -> None:
    global temp
    temp = new_temp


def admin_get_temp() -> float:
    return temp


def create_promt(user_promt, admin_promt=__system_promt__):
    if len(str(user_promt)) == 0 or user_promt is None:
        return None

    return {
        "modelUri": "gpt://{}/yandexgpt/latest".format(__storage_id__),
        "completionOptions": {
            "stream": False,
            "temperature": temp,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": admin_promt
            },
            {
                "role": "user",
                "text": user_promt
            }
        ]
    }


def get_response_mark(text: str) -> int:
    promt = create_promt(user_promt=text)

    response = requests.post(url=__url__, headers=__headers__, json=promt).json()
    try:
        mark = response['result']['alternatives'][0]['message']['text']
    except:
        return 0

    try:
        int_mark = int(mark)
        return int_mark
    except:
        return 0

