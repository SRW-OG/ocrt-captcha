===
*修订记录*

| 编号 | 日期 | 修订内容 |
|---|---|---|
| 1 | 2020.07.21 | 初稿 |
|   |   |   |


*目录*
@toc

---
利用已知轮子组合，本方法优点：
- 使用本地 OCR 图片识别
- 代码量小
- 验证码识别正确率较高

# 工具和环境
## muggle-ocr
这是一个存在训练模型的使用机器学习识别验证码的 python 模块
地址：
[https://pypi.org/project/muggle-ocr/](https://pypi.org/project/muggle-ocr/)

## captcha-killer
`captcha-killer`要解决的问题是让burp能用上各种验证码识别技术，是一个 burp 的插件

# 自定义图形验证码接口


安装依赖`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

安装相应的依赖后，编写`app.py`，内容如下：


请求验证码接口固定的请求参数，这部分直接复制到
```
POST /api/v1/ocr-captcha HTTP/1.1
Host: 10.211.55.3:8001
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 0

image=<@URLENCODE><@BASE64><@IMG_RAW></@IMG_RAW></@BASE64></@URLENCODE>
```


# 验证码爆破

登录窗口

