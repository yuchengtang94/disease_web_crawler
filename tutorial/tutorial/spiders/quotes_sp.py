import scrapy
import re

class AuthorSpider(scrapy.Spider):
    name = 'rare_disease'

    start_urls = ['https://rarediseases.org/for-patients-and-families/information-resources/rare-disease-information/']
    i = 0;
    # reg = re.compile('<[^>]*>')
    def parse(self, response):
        # follow links to author pages
        for href in response.css('.rare-diseases a::attr(href)'):
            # print(href + '#causes')
            # if href is not None:
            # page = response.urljoin(href)
            # yield scrapy.Request(page, callback=self.parse_disease)
            # print(response)
            yield response.follow(href, self.parse_disease)

        # follow pagination links
        next_page = response.css('.pagination .next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


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
        introduction_rawData = extract_with_css('#general-discussion')
        symptoms_rawData = extract_with_css('#symptoms')
        causes_rawData = extract_with_css('#causes')
        treatment_rawData = extract_with_css('#standard-therapies')
        introduction = remove_html(introduction_rawData)
        symptoms = remove_html(symptoms_rawData)
        causes = remove_html(causes_rawData)
        treatment = remove_html(treatment_rawData)


        
        yield {
            'id' : self.i,
            # 'name': extract_with_css('body > div.white-wrapper.rdr-single-wrp > div.container.single-reports-container > div > div.col-lg-8.col-md-8.col-sm-8.col-xs-12.print-only > h3::text'),
            # 'introduction_rawData': introduction_rawData,
            # 'symptoms_rawData': symptoms_rawData,
            # 'causes_rawData': causes_rawData,
            # 'treatment_rawData': treatment_rawData,
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

        

# scrapy crawl rare_disease -o rare_disease.json
# response.css('.pagination ul:last-child a::attr(href)').extract_first()

