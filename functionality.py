from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


def collect_data():

    ua = UserAgent()

    with open("all_lots.txt", "w", encoding="utf-8") as file:
    # with open("smthsht.html", "w", encoding="utf-8") as file:
    #     file.write(src)
        for i in range(1, 5):
            url = f"https://violity.com/auction/287-faleristika-sssr?show_type=6&order=10&utm_source=sorting_new_lots&utm_medium=sorting_last_action&page={i}"
            req = requests.get(url, headers={"user-agent": f"{ua.random}"})
            src = req.text
            soup = BeautifulSoup(src, "lxml")
            all_lots = soup.find_all("div", class_="title")
            for lot in all_lots:
                try:
                    lot_text = lot.text
                    lot_url = lot.find("a").get("href")

                    file.write(f"{lot_text} -- {lot_url}\n")
                except:
                    None


def main():
    collect_data()


if __name__ == "__main__":
    main()