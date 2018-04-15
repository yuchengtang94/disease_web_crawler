import scrapy
import re

class AuthorSpider(scrapy.Spider):
    name = 'disease'

    start_urls = ['https://www.nhsinform.scot/illnesses-and-conditions/a-to-z']
    i = 0;
    # reg = re.compile('<[^>]*>')
    def parse(self, response):
        # follow links to author pages
        for href in response.css('.blockgrid-item + a::attr(href)'):
            # print(href + '#causes')
            # if href is not None:
            # page = response.urljoin(href)
            # yield scrapy.Request(page, callback=self.parse_disease)
            # print(response)
            yield response.follow(href, self.parse_disease)

        # follow pagination links
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, self.parse)


    def parse_disease(self, response):
        self.i = self.i + 1
        # print(response)
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        def remove_html(query):
            reg = re.compile('<[^>]*>')
            return reg.sub(' ' , query).strip()
        # yield response.follow('#causes', self.parse_info)
        # for href in response.css('.blockgrid-item + a::attr(href)'):
            # yield response.follow('#symptoms', self.parse_disease)
        # symptom = response.follow('#symptoms', self.parse_info)
        # print('xxxxxxxxxxxxxxxxxxxx')
        # yield response.follow('#symptoms', self.parse_info)
        # symptom = ''
        # yield response.follow('#causes', self.parse_info)
        # page = response.urljoin('#causes')
        # yield scrapy.Request(page, callback=self.parse_info, dont_filter=True)
        # # yield response.follow('#symptoms', self.parse_info, dont_filter=True)
        introduction_rawData = extract_with_css('#introduction > div')
        symptoms_rawData = extract_with_css('#symptoms > div')
        causes_rawData = extract_with_css('#causes > div')
        treatment_rawData = extract_with_css('#treatment > div')
        introduction = remove_html(introduction_rawData)
        symptoms = remove_html(symptoms_rawData)
        causes = remove_html(causes_rawData)
        treatment = remove_html(treatment_rawData)


        
        yield {
            'id' : self.i,
            # 'name': extract_with_css('.js-guide-title::text'),
            # 'introduction_rawData': extract_with_css('#introduction > div'),
            # 'symptoms_rawData': extract_with_css('#symptoms > div'),
            # 'causes_rawData': extract_with_css('#causes > div'),
            # 'treatment_rawData': extract_with_css('#treatment > div'),
            'introduction': introduction,
            'symptoms': symptoms,
            'causes': causes,
            'treatment': treatment,
        }
    # def parse_info(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).extract_first().strip()
    #     print('***************')
    #     # return extract_with_css('div.editor')
    #     symptom = extract_with_css('.editor::text')
    #     symptom = '11111'
    #     print(symptom)
    #     yield {
    #         'name': extract_with_css('.js-guide-title::text'),
    #         # 'introduction': extract_with_css('#introduction.editor::text'),
    #         'causes': extract_with_css('.editor::text'),
    #     }
    #     # yield extract_with_css('.editor::text')

        

# scrapy crawl disease -o disease.json

