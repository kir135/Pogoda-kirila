import requests
import os

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            print(f"\n--- Погода в городе {city} ---")
            print(f"Температура: {temp}°C (ощущается как {feels_like}°C)")
            print(f"Описание: {description.capitalize()}")
            print(f"Влажность: {humidity}%")
            print(f"Скорость ветра: {wind_speed} м/с")
        else:
            print(f"Ошибка {response.status_code}: {data.get('message', 'Неизвестная ошибка')}")
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения к интернету. Проверьте сеть.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Пожалуйста, установите переменную окружения OPENWEATHER_API_KEY с вашим API-ключом.")
        print("Или вставьте ключ прямо в код (небезопасно для публичных репозиториев).")
        return
    city = input("Введите название города (например, Moscow): ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
