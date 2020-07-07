from baidubaike import url_manager, html_download, html_output, html_parser


class SpiderMan():
    def __init__(self):
        self.urls = url_manager.urlManmager()
        self.downloader = html_download.htmlDownloader()
        self.outputer = html_output.htmlOutputer()
        self.parser = html_parser.htmlParser()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('count:%d  url:%s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                url_count = self.urls.get_url_count()
                print(url_count)
                if count >= 100:
                    break
                count = count + 1
            except Exception as e:
                print(str(e))
                # 根据报错信息提示错误

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMan()
    obj_spider.craw(root_url)

