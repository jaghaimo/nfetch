import argparse

import requests
from bs4 import BeautifulSoup
from rich.progress import track


def get_chapter(novel: str, chapter: int) -> str:
    r = requests.get(f"https://boxnovel.com/novel/{novel}/chapter-{chapter}/")
    soup = BeautifulSoup(r.content, features="html.parser")
    for script in soup.find_all("script"):
        script.extract()
    return soup.find_all("div", {"class": "entry-content"}).pop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--novel-title", required=True, type=str)
    parser.add_argument("-f", "--first-chapter", required=True, type=int)
    parser.add_argument("-l", "--last-chapter", required=True, type=int)
    args = parser.parse_args()
    print("Downloading chapters...")
    for chapter in track(range(args.first_chapter, args.last_chapter + 1)):
        content = get_chapter(args.novel_title, chapter)
        output_filename = f"{args.novel_title}-{chapter:05d}.html"
        with open(output_filename, "w") as f:
            f.write(str(content))
