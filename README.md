# Пакет для работы с поисковыми системами Google, Yandex через сервис xmlriver.com

*English description below*


Привет! Добро пожаловать на страницу пакета xmlriver, который позволяет взаимодействовать по API с сервисом xmlriver.com и получать результаты выдачи из поисковых систем Яндекс и Google.

## Установка

    pip install xmlriver

## Использование

    import xmlriver
    user = 000 #Ваш user_id со страницы https://xmlriver.com/queries/
    key = '' #Ваш ключ со страницы https://xmlriver.com/queries/
    google = xmlriver.Google(user, key)
    query = 'Ваш запрос'
    if google.query(query):
	    print(google.results)

## Дополнительные параметры
Вы можете передавать дополнительные параметры, которые представлены на странице https://xmlriver.com/apidoc/api-about/ (для Google) и https://xmlriver.com/apiydoc/apiy-about/ (для Яндекс)

**Пример передачи параметров:**

    google = xmlriver.Google(user, key, country=10, device='desktop')

Или прямо в запросе:

    google.query(query, country=10, device='desktop')

## Доступные методы и атрибуты
 1. google.get_balance() - Получить информацию о балансе
 2. google.get_cost() - Получить стоимость за 1 000 запросов
 3. google.query(query, **kwargs) - Отправить запрос к Google
 4. google.pages - Число, количество найденных результатов
 5. google.results - Список найденных документов
 6. google.get_urls() - Список найденных URL
 7. google.get_titles() - Список заголовков результатов поисковой выдачи
 8. google.get_results_with_domain(domain, **kwargs) - Аналог запроса "domain" -site:domain. Выводит количество результатов
 9. google.is_trust_domain(domain, **kwargs) - Простая проверка домена на траст. True / False
 10. google.is_url_pessimised(url, **kwargs) - Проверка url на наличие фильтра - True / False. Перед этим проверьте, что URL проиндексирован
 11. google.is_url_indexed(url, **kwargs) - Проверка url на индексацию

## Поддержка
xmlriver использует пакеты requests и xmltodict и должен работать везде, где работает Python.

## Автор
Иван Шарков
Мой блог https://0pl.ru
Моя организация: https://kurshub.ru



# Package for working with search engines Google, Yandex via xmlriver.com service


Hi! Welcome to the xmlriver package page, which allows you to interact via API with xmlriver.com service and get results from Yandex and Google search engines.

## Install

    pip install xmlriver

## Usage

    import xmlriver
    user = 000 #Your user_id from the page https://xmlriver.com/queries/
    key = '' #Your key from page https://xmlriver.com/queries/
    google = xmlriver.Google(user, key)
    query = 'Your query'
    if google.query(query):
	    print(google.results)

## Additional parameters
You can pass additional parameters, which can be found at https://xmlriver.com/apidoc/api-about/ (for Google) and https://xmlriver.com/apiydoc/apiy-about/ (for Yandex).

**Example of passing parameters:**

    google = xmlriver.Google(user, key, country=10, device='desktop')

Or directly in the query:

    google.query(query, country=10, device='desktop')

## Available methods and attributes
 1. google.get_balance() - Get balance information
 2. google.get_cost() - Get cost per 1,000 queries
 3. google.query(query, **kwargs) - Send a query to Google
 4. google.pages - Number, number of results found
 5. google.results - List of documents found
 6. google.get_urls() - List of URLs found
 7. google.get_titles() - List of titles of search results
 8. google.get_results_with_d
 9. google.is_trust_domain(domain, **kwargs) - Simple domain trust check. True / False
 10. google.is_url_pessimized(url, **kwargs) - Check url for filter - True / False. Before doing this, check that the url is indexed
 11. google.is_url_indexed(url, **kwargs) - Check url for indexing

## Support
xmlriver uses the requests and xmltodict packages and should work wherever Python is running.

## Author
Ivan Sharkov
My blog: https://0pl.ru
My organization: https://kurshub.ru