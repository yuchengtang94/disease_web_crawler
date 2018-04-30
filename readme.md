# Scrapy crawler Collect Disease Infomation

Author: Yucheng Tang

This is a part of our elastic_search disease search engine project!

After running the following command, you will get datas you need for search engine.


```
cd tutorial

scrapy crawl disease -o disease.json
scrapy crawl rare_disease -o rare_disease.json

python process.py
```

Data all in tutorial folder

