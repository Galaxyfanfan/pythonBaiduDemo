import re
import urllib.parse
from bs4 import BeautifulSoup
#网页解析器
class htmlParser(object):
    def parse(self,page_url,html_cont):
        if page_url == None or html_cont == None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        new_urls = self.get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_urls,new_data

    def get_new_urls(self,page_url,soup):
        links = soup.find_all("a",href = re.compile(r"/item/"))
        new_urls = set()
        for link in links:
            # print(link)
            new_url = link["href"]
            #拼接url
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            # print("new_full_url：" + new_full_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}
        res_data["url"] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd",class_ = "lemmaWgt-lemmaTitle-title").find("h1")

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div",class_ = "lemma-summary")

        res_data["title"] = title_node
        res_data["summary"] = summary_node

        return res_data

