import requests

def fetch_wikipedia_article(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверка на HTTP-ошибки

        print("Запрос выполнен успешно!")
        print("Первые 500 символов статьи:")
        print(response.text[:500])
    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания ответа.")
    except requests.exceptions.ConnectionError:
        print("Ошибка подключения. Проверьте интернет-соединение или адрес сайта.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Произошла ошибка при выполнении запроса: {err}")

article_url = "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"
fetch_wikipedia_article(article_url)

