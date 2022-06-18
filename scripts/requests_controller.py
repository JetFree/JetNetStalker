from scripts.os_utils import get_dir_size
from bs4 import BeautifulSoup
from colorama import Fore
import requests
import re
from datetime import datetime


def is_host_available(url):
    try:
        if requests.get(url, timeout=2).status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False


def check_condition(condition, counter_link):
    method, method_value = condition.popitem()
    if method == "time":
        return datetime.now() > method_value
    elif method == "links":
        return counter_link.value >= method_value
    elif method == "size":
        return get_dir_size() >= method_value


def check_url(condition, link_counter, event, host, page_id):
    if check_condition(condition, link_counter):
        event.set()
    if event.is_set():
        return
    full_url = host + "/gallery/" + "".join(page_id)
    try:
        if is_page_exists(resp := requests.get(full_url, timeout=3).text):
            print(Fore.GREEN + "Good! --> " + Fore.RESET + full_url)
            save_file(parse_url(resp))
            link_counter.value += 1
            return full_url
        else:
            print(full_url)
    except Exception as e:
        print(e)


def parse_url(html_page):
    soup = BeautifulSoup(html_page, "html.parser")
    if elem := soup.find("meta", attrs={"property": "og:video:secure_url"}):
        return elem["content"]
    elif result := re.search("content=\"(https:\/\/i\.imgur\.com\/[a-zA-z0-9]{4,8}\.[a-zA-Z0-9]{3,6})", html_page):
        return result.group(1)
    else:
        print("Can't find what to download on the page")


def is_page_exists(html):
    bs4 = BeautifulSoup(html, "html.parser")
    if bs4.find("title"):
        return True
    else:
        return False


def save_file(url):
    try:
        file_name = url.split("/")[-1]
        res = requests.get(url, stream=True)
        res.raise_for_status()
        with open("./downloads/" + file_name, "wb") as file:
            for i in res.iter_content(chunk_size=64000):
                file.write(i)
    except Exception as e:
        print(e)
