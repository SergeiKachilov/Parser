import requests
import re

link = "https://tagil-tv.ru/"
html = requests.get("https://www.tagil-tv.ru/news").text

r = re.findall(
    r"<div class=\"views-field views-field-title\">\s+<span class=\"field-content\"><a href=\"(.+)\">[&quot;]*(.+[^&quot;]).*</a></span>\s+</div>\s+<div class=\"views-field views-field-field-news-body\">\s+<span class=\"field-content\">(.+)</span>\s+</div>\s+<div class=\"views-field views-field-created-1\">\s+<span class=\"field-content\">(.+)\.(.+)\.(.+)</span>\s+</div>",
    html,
)

with open("Tagil news.txt", "w", encoding="utf-8") as f:
    for i in r:
        n_link = link + i[0]
        title = i[1]
        subTitle = i[2]
        day = i[3]
        month = i[4]
        year = i[5]

        f.write(
            f"Заголовок: {title}\nОписание: {subTitle}\nСсылка: {n_link}\nДата: {day}.{month}.{year}\n\n".ljust(
                10
            )
        )
