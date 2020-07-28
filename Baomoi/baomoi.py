import scrapy

class Zing(scrapy.Spider):
    name = "Zing"
    urls = ['https://zingnews.vn/hai-benh-nhan-covid-19-o-quang-ngai-tien-trien-tich-cuc-post1112414.html',]

    def parse(self, response):
        f = open('D:\\PyCharm\\CodePythyon\\Baomoi\\Output\\Test1.txt', 'wb+')
        title = response.css('h1.the-article-title::text').get()
        f.write(title.strip() + '\n')
        f.close()
        summary = response.css('p.the-article-summary::text').get()
        f.write(summary.strip() + '\n')
        f.close()
        for i in response.css('p.the-article-body::text'):
            p_body = i.get()
            f.write(p_body.strip() + '\n')
            f.close()
        yield {
            "Tiêu đề" : response.css('h1.the-article-title::text').get(),
            "Giới thiệu" : response.css('p.the-article-summary::text').get(),
        }

