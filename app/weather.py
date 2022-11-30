import sys

from pyowm import OWM
#from pyowm.exceptions.api_response_error import UnauthorizedError


# Чтобы получить свой собственный ключ для доступа к API OWM:
# 1. зарегистрируйся на https://openweathermap.org/;
# 2. сгенерируй ключ здесь: https://home.openweathermap.org/api_keys
# 3. поменяй значение в строке ниже:
API_key = '6e67a535c806a2f41ae2b5b8e605cdd5'

owm = OWM(API_key)
place = input("Введите город: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature("celsius")
t1 = temp['temp']
t2 = temp['feels_like']

print(f"Сегодня у тебя {t1}℃, а ощущается как {t2}")



'''
try:
    owm.is_API_online()
except UnauthorizedError:
    print("Упс! Кажется, ключ доступа к API OpenWeatherMap неправильный!")
    print(f"Вставь правильный токен в {__file__}!")
    sys.exit(1)

city_name = input("Введи название своего города (на английском): ")
reg = owm.city_id_registry()
variants = reg.ids_for(city_name)

if len(variants) == 1:
    city_id = variants[0][0]
else:
    while True:
        try:
            print("Какой именно город?")
            for i, (_, variant_city, variant_country) in enumerate(variants):
                print(f"{i}) {variant_city}, {variant_country}")

            # здесь может возникнуть ValueError
            choice = int(input("Введи номер варианта (число): "))

            # здесь может возникнуть IndexError
            city_id = variants[choice][0]

            # если ошибок не возникло, то выходим из бесконечного цикла
            break
        except (ValueError, IndexError):
            print("Не понял тебя! Давай попробуем еще раз!")

obs = owm.weather_at_id(city_id)
w = obs.get_weather()

t = w.get_temperature(unit="celsius")["temp"]
status = w.get_status()

print(f"Сегодня у тебя {t}℃, а в целом дела обстоят вот так: {status}")'''