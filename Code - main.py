import requests
from bs4 import BeautifulSoup
import pandas as pd

stars=[]
titles=[]
contents=[]

for page in range(2,12):
    url = f"https://www.amazon.com/Ring-Alarm-Pro-8-piece-kit/product-reviews/B08HSTJPM5/ref=cm_cr_arp_d_paging_btm_next_{page}?ie=UTF8&reviewerType=all_reviews&pageNumber={page}"
    headers = {
        "Accept-Language": "sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")

    reviews = soup.find_all(name="div", class_="review")
    for review in reviews:
        star = review.find(name="span", class_="a-icon-alt").get_text().split(" ")[0]
        title = review.find(name="a", class_="review-title").find(name="span").getText()
        content = review.find(name="span", class_="review-text-content").find(name="span").getText()

        stars.append(star)
        titles.append(title)
        contents.append(content)

review_dict = {
    "Rating": stars,
    "Title": titles,
    "Text": contents,
}
item1 = pd.DataFrame(review_dict)
item1.to_csv("Data - item1.csv", index=False)

