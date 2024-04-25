import time
from requests import get
import re
from datetime import datetime
from text_scrapper import get_text_from_url, get_title_from_url

min_urls = [
    ['https://eco.tatarstan.ru/', 'Министерство экологии Республики Татарстан'],
    ['https://mtsz.tatarstan.ru/', 'Минтруда Республики Татарстан'],
    ['https://minmol.tatarstan.ru/index.htm', 'Минмолодежи Республики Татарстан'],
    ['https://mzio.tatarstan.ru/index.htm', 'Минземимущества Республики Татарстан'],
    ['https://minleshoz.tatarstan.ru/index.htm', 'Министерство лесного хозяйства Республики Татарстан'],
    ['https://minsport.tatarstan.ru/index.htm', 'Министерство спорта Республики Татарстан'],
    ['https://mpt.tatarstan.ru/index.htm', 'Министерство промышленности и торговли Республики Татарстан'],
    ['https://agro.tatarstan.ru/index.htm', 'Министерство сельского хозяйства Республики Татарстан'],
    ['https://minstroy.tatarstan.ru/index.htm', 'Министерство строительства и архитектуры Республики Татарстан'],
    ['https://mindortrans.tatarstan.ru/index.htm', 'Миндортранс Республики Татарстан'],
    ['https://eco.tatarstan.ru/index.htm', 'Министерство экологии Республики Татарстан'],
    ['https://zags.tatarstan.ru/index.htm', 'Управление ЗАГС по Республике Татарстан'],
    ['https://mert.tatarstan.ru/', 'Министерство экономики Республики Татарстан'],
    ['https://minfin.tatarstan.ru/', 'Министерство финансов Республики Татарстан'],
    ['https://minjust.tatarstan.ru/', 'Министерство юстиции Республики Татарстан'],
    ['https://digital.tatarstan.ru/', 'Министерство цифрового развития Республики Татарстан'],
    ['https://prav.tatarstan.ru/', 'Правительство Республики Татарстан'],
    ['https://mincult.tatarstan.ru/', 'Министерство культуры Республики Татарстан'],
    ['https://minsport.tatarstan.ru/', 'Министерство спорта Республики Татарстан'],
    ['https://minzdrav.tatarstan.ru/', 'Министерство здравоохранения Республики Татарстан'],
    ['https://mon.tatarstan.ru/', 'Министерство образования Республики Татарстан'],
    ['https://tida.tatarstan.ru/', 'Агентство инвестиционного развития Республики Татарстан'],
    ['https://gossov.tatarstan.ru/', 'Государственный совет Республики Татарстан'],
    ['https://mchs.tatarstan.ru/', 'МЧС Республики Татарстан'],
    ['https://arhiv.tatarstan.ru/index.htm', 'Государственный комитет Республики Татарстан по архивному делу'],
    ['https://goszakupki.tatarstan.ru/index.htm', 'Государственный комитет Республики Татарстан по закупкам'],
    ['https://kt.tatarstan.ru/index.htm', 'Государственный комитет Республики Татарстан по тарифам'],
    ['https://tourism.tatarstan.ru/index.htm', 'Государственный комитет Республики Татарстан по туризму'],
    ['https://ojm.tatarstan.ru/index.htm', 'Государственный комитет Республики Татарстан по биологическим ресурсам'],
    ['https://okn.tatarstan.ru/index.htm',
     'осударственный комитет Республики Татарстан по охране объектов культурного наследия'],
    ['https://agryz.tatarstan.ru/', 'Агрызский муниципальный район Республики Татарстан'],
    ['https://aznakayevo.tatarstan.ru/', 'Азнакаевский муниципальный район Республики Татарстан'],
    ['https://aksubayevo.tatarstan.ru/', 'Аксубаевский муниципальный район Республики Татарстан'],
    ['https://aktanysh.tatarstan.ru/', 'Актанышский муниципальный район Республики Татарстан'],
    ['https://alekseevskiy.tatarstan.ru/', 'Алексеевский муниципальный район Республики Татарстан'],
    ['https://alkeevskiy.tatarstan.ru/', 'Алькеевский муниципальный район Республики Татарстан'],
    ['https://almetyevsk.tatarstan.ru/', 'Альметьевский муниципальный район Республики Татарстан'],
    ['https://apastovo.tatarstan.ru/', 'Апастовский муниципальный район Республики Татарстан'],
    ['https://arsk.tatarstan.ru/', 'Арский муниципальный район Республики Татарстан'],
    ['https://atnya.tatarstan.ru/', 'Атнинский муниципальный район Республики Татарстан'],
    ['https://bavly.tatarstan.ru/', 'Бавлинский муниципальный район Республики Татарстан'],
    ['https://baltasi.tatarstan.ru/', 'Балтасинский муниципальный район Республики Татарстан'],
    ['https://bugulma.tatarstan.ru/', 'Бугульминский муниципальный район Республики Татарстан'],
    ['https://buinsk.tatarstan.ru/', 'Буинский муниципальный район Республики Татарстан'],
    ['https://verhniy-uslon.tatarstan.ru/', 'Верхнеуслонский муниципальный район Республики Татарстан'],
    ['https://vysokaya-gora.tatarstan.ru/', 'Высокогорский муниципальный район Республики Татарстан'],
    ['https://drogganoye.tatarstan.ru/', 'Дрожжановский муниципальный район Республики Татарстан'],
    ['https://zainsk.tatarstan.ru/', 'Заинский муниципальный район Республики Татарстан'],
    ['https://zelenodolsk.tatarstan.ru/', 'Зеленодольский муниципальный район Республики Татарстан'],
    ['https://kaybici.tatarstan.ru/', 'Кайбицкий муниципальный район Республики Татарстан'],
    ['https://kamskoye-ustye.tatarstan.ru/', 'Камско-Устьинский муниципальный район Республики Татарстан'],
    ['https://kukmor.tatarstan.ru/', 'Кукморский муниципальный район Республики Татарстан'],
    ['https://laishevo.tatarstan.ru/', 'Лаишевский муниципальный район Республики Татарстан'],
    ['https://leninogorsk.tatarstan.ru/', 'Лениногорский муниципальный район Республики Татарстан'],
    ['https://mamadysh.tatarstan.ru/', 'Мамадышский муниципальный район Республики Татарстан'],
    ['https://mendeleevsk.tatarstan.ru/', 'Менделеевский муниципальный район Республики Татарстан'],
    ['https://menzelinsk.tatarstan.ru/', 'Мензелинский муниципальный район Республики Татарстан'],
    ['https://muslumovo.tatarstan.ru/', 'Муслюмовский муниципальный район Республики Татарстан'],
    ['https://novosheshminsk.tatarstan.ru/', 'Новошешминский муниципальный район Республики Татарстан'],
    ['https://nurlat.tatarstan.ru/', 'Нурлатский муниципальный район Республики Татарстан'],
    ['https://pestreci.tatarstan.ru/', 'Пестречинский муниципальный район Республики Татарстан'],
    ['https://ribnaya-sloboda.tatarstan.ru/', 'Рыбно-Слободский муниципальный район Республики Татарстан'],
    ['https://saby.tatarstan.ru/', 'Сабинский муниципальный район Республики Татарстан'],
    ['https://sarmanovo.tatarstan.ru/', 'Сармановский муниципальный район Республики Татарстан'],
    ['https://spasskiy.tatarstan.ru/', 'Спасский муниципальный район Республики Татарстан'],
    ['https://tetushi.tatarstan.ru/', 'Тетюшский муниципальный район Республики Татарстан'],
    ['https://tukay.tatarstan.ru/', 'Тукаевский муниципальный район Республики Татарстан'],
    ['https://tulachi.tatarstan.ru/', 'Тюлячинский муниципальный район Республики Татарстан'],
    ['https://cheremshan.tatarstan.ru/', 'Черемшанский муниципальный район Республики Татарстан'],
    ['https://chistopol.tatarstan.ru/', 'Чистопольский муниципальный район Республики Татарстан'],
    ['https://jutaza.tatarstan.ru/', 'Ютазинский муниципальный район Республики Татарстан'],
    ['https://gji.tatarstan.ru/index.htm', 'Государственная жилищная инспекция Республики Татарстан'],
    ['https://guv.tatarstan.ru/index.htm', 'Главное управление ветеринарии Республики Татарстан'],
    ['https://fpd.tatarstan.ru/index.htm', 'ГБУ «Фонд пространственных данных Республики Татарстан»'],
    ['https://kremlin.tatarstan.ru/index.htm', 'ГБУ «Музей-заповедник «Казанский кремль»'],
    ['https://gisu.tatarstan.ru/index.htm', 'Главное инвестиционно-строительное управление Республики Татарстан'],
    ['https://gosalcogol.tatarstan.ru/index.htm', 'Госалкогольинспекция Республики Татарстан'],
    ['https://gbubdd.tatarstan.ru/index.htm', 'ГБУ «Безопасность дорожного движения» Республики Татарстан'],
    ['https://dorogi.tatarstan.ru/index.htm', 'ГКУ «Главтатдортранс»'],
    ['https://obrnadzor.tatarstan.ru/index.htm',
     'Департамент надзора и контролся в сфере образования Республики Татарстан'],
    ['https://gsn.tatarstan.ru/index.htm', 'Гостройнадзор Республики Татарстан'],
    ['https://rkdnrt.tatarstan.ru/index.htm',
     'Государственная комиссия по делам несовершеннолетних Республики Татарстан'],
    ['https://zemlya.tatarstan.ru/', 'Центр развития земельных отношений Республики Татарстан'],
    ['https://ivf.tatarstan.ru/index.htm', 'Инвестиционно-венчурный фонд Республики Татарстан'],
    ['https://ttp.tatarstan.ru/', 'Татарстанская транспортная прокуратура'],
    ['https://usd.tatarstan.ru/index.htm', 'Управление судебного департамента Республики Татарстан'],
    ['https://gibdd.tatarstan.ru/index.htm', 'Управление ГИБДД по Республике Татарстан'],
    ['https://rosgvard.tatarstan.ru/index.htm', 'Управление Росгвардии по Республике Татарстан'],
    ['https://gtn.tatarstan.ru/', 'Гостехнадзор по Республике Татарстан'],
    ['https://ombudsmanbiz.tatarstan.ru/index.htm', 'Бизнесомбудсмен Республики Татарстан'],
    ['https://rtdety.tatarstan.ru/index.htm', 'Детский омбудсмен Республики Татарстан'],
    ['https://upch.tatarstan.ru/index.htm', 'Уполномоченный по правам человека Республики Татарстан'],
    ['https://izbirkom.tatarstan.ru/', 'ЦИК Республики Татарстан'],
    ['https://potrebiteli.tatarstan.ru/index.htm', 'Союз потребителей Республики Татарстан'],
    ['https://rsmrt.tatarstan.ru/index.htm', 'Татарстанская региональная организация «Российского союза молодежи»'],
    ['https://germany.tatarstan.ru/', 'Торгово-экономическое представительство Республики Татарстан в городе Лейпциге'],
    ['https://china.tatarstan.ru/index.htm', 'Торгово-экономическое представительство Республики Татарстан в Китае'],
    ['https://cuba.tatarstan.ru/index.htm', 'Торгово-экономическое представительство Республики Татарстан на Кубе'],
    ['https://saratov.tatarstan.ru/index.htm',
     'Торгово-экономическое представительство Республики Татарстан в Саратовской области'],
    ['https://suomi.tatarstan.ru/index.htm',
     'Торгово-экономическое представительство Республики Татарстан в Финляндии'],
    ['https://swiss.tatarstan.ru/index.htm',
     'Торгово-экономическое представительство Республики Татарстан в Швейцарии'],
    ['https://tatmsk.tatarstan.ru/index.htm',
     'Полномочное представительство Республики Татарстан в Российской Федерации'],
    ['https://kz.tatarstan.ru/index.htm', 'Полномочное представительство Республики Татарстан в Казахстане'],
    ['https://tatturkmen.tatarstan.ru/index.htm', 'Полномочное представительство Республики Татарстан в Туркменистане'],
    ['https://tatturk.tatarstan.ru/index.htm', 'Полномочное представительство Республики Татарстан в Турции'],
    ['https://france.tatarstan.ru/index.htm', 'Полномочное представительство Республики Татарстан во Франции'],
    ['https://az.tatarstan.ru/index.htm', 'Постоянное представительство Республики Татарстан в Азербайджане'],
    ['https://postpredrb.tatarstan.ru/index.htm', 'Постоянное представительство Республики Татарстан в Башкортостане'],
    ['https://postpredrk.tatarstan.ru/index.htm',
     'Постоянное представительство Республики Татарстан в Крыму и Севастополе'],
    ['https://tatspb.tatarstan.ru/index.htm',
     'Постоянное представительство Республики Татарстан в Санкт-Петербурге и Ленобласти'],
    ['https://tatur.tatarstan.ru/index.htm',
     'Постоянное представительство Республики Татарстан в Свердловской области'],
    ['https://prtuz.tatarstan.ru/index.htm', 'Представительство Республики Татарстан в Узбекистане'],
    ['https://dubai.tatarstan.ru/index.htm', 'Торгово-экономическое представительство Республики Татарстан в Дубае'],
    ['https://torgprednn.tatarstan.ru/index.htm',
     'Торгово-экономическое представительство Республики Татарстан в Нижегородской области'],
    ['https://ugra.tatarstan.ru/index.htm',
     'Торгово-экономическое представительство Республики Татарстан в ХМАО - Югре'],
    ['https://czech.tatarstan.ru/index.htm', 'Торгово-экономическое представительство Республики Татарстан в Чехии']
]


def stop_filter(title: str, content: str) -> bool:
    if len(title) < 30 or len(content) < 300:
        return True

    blacklist = ['информирует', 'анонс', 'погода', 'погоды', 'погодны', 'приглашает', 'приглашают',
                 'приглашаем', 'субботник', 'уборк', 'конкурс']

    if any(b_word in str(title).lower() for b_word in blacklist):
        return True

    return False


def get_all_news_urls(url: str, date: str) -> []:
    url = url.strip()

    if not url.startswith('https://'):
        url = 'https://' + url.strip()

    if url.endswith('/'):
        pos = url.rfind('/')
        url = url[:pos]
    if url.endswith('/index.htm'):
        pos = url.rfind('/index.htm')
        url = url[:pos]

    try:
        response = get(url + f'/index.htm/news/{date}.htm', timeout=(0.1, 10))
    except:
        return []

    if response.status_code != 200:
        return []

    response_text = response.text

    start_filter = "<a href='/index.htm/news/"
    links = []

    matches = re.findall(start_filter + r'\d+' + '.htm', response_text)

    for match in matches:
        links.append(url + str(match).replace("<a href='", ""))

    return links


async def start_min_parser(send_news_func):
    link_list = []
    global min_urls
    while True:
        date = datetime.today().date()
        write_date = str(date).split('-')[2] + '/' + str(date).split('-')[1] + '/' + str(date).split('-')[0]
        for min_item in min_urls:
            url = min_item[0]
            min_name = min_item[1]
            links = get_all_news_urls(url, str(date))
            if links is None or links == []:
                continue
            for link in links:
                if link is None:
                    continue
                if link in link_list:
                    continue
                link_list.append(link)

                if len(link_list) > 1000:
                    link_list = []

                title = get_title_from_url(link)
                content = get_text_from_url(link)

                if content is None or title is None:
                    continue

                if stop_filter(title=str(title), content=str(content)):
                    continue

                await send_news_func(
                    title=title.strip(),
                    min_name=min_name.strip(),
                    date=write_date.strip(),
                    content=content.strip(),
                    link=str(link).strip()
                )

                time.sleep(2)
