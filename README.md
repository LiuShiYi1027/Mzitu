# 妹子图爬虫
> 更新于2018年04月24日
## Target Site: 
    https://www.mzitu.com
## 环境：
1. Python3.6.3
2. Scrapy1.5.0
3. pymongo3.6.1

## 版本

### V1(完成于2018年04月24日) 

#### 版本功能：

1. 爬取mzitu全站图片，以套图为单位进行存储
2. 将爬取的信息存储在mongo数据库中

   > 爬取的信息包括：
   - 组图名称:title
   - 组图包含图片的数量:num
   - 组图的入口地址:url
   - 每一张图片的相信url:image_urls
   
   例如：
   ```json
   "root":{
        "_id":"5adee9aab99c5d03abb6213c"
        "url":"http://www.mzitu.com/127125"
        "title":"巨乳御姐白一晗火辣的肉体性感爆棚"
        "num":40
        "image_urls":[
            "http://i.meizitu.net/2018/04/23b24.jpg"
            "http://i.meizitu.net/2018/04/23b23.jpg"
            "http://i.meizitu.net/2018/04/23b22.jpg"
            "http://i.meizitu.net/2018/04/23b40.jpg"
            "http://i.meizitu.net/2018/04/23b39.jpg"
            "http://i.meizitu.net/2018/04/12b16.jpg"
            "http://i.meizitu.net/2018/04/12b15.jpg"
            "http://i.meizitu.net/2018/04/12b14.jpg"
            "http://i.meizitu.net/2018/04/12b13.jpg"
            "http://i.meizitu.net/2018/04/12b12.jpg"
            "http://i.meizitu.net/2018/04/11b34.jpg"
            "http://i.meizitu.net/2018/04/11b50.jpg"
            "http://i.meizitu.net/2018/04/11b49.jpg"
            "http://i.meizitu.net/2018/04/11b48.jpg"
            "http://i.meizitu.net/2018/04/11b47.jpg"
            "http://i.meizitu.net/2018/04/11b46.jpg"
            "http://i.meizitu.net/2018/04/11b45.jpg"
            "http://i.meizitu.net/2018/04/11b44.jpg"
            "http://i.meizitu.net/2017/05/07a36.jpg"
        ]
    }
    ```
#### 使用方式
1. 在'settings.py'文件中修改'IMAGES_STORE'字段值，设置图片存储路径IMAGES_STORE；
2. 开启mongodb数据库（数据库会自动创建）
3. 使用python3.6.3运行'run.py'文件
   
#### 反爬机制手记
目标网站使用"防盗链"机制，对图片url发起请求时需关注http请求中的"referer"字段
 
   



 