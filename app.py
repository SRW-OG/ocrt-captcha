# -*- coding: utf-8 -*-

import os
import sys
import time
import base64

import muggle_ocr

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'API说明：post image=<@URLENCODE><@BASE64><@IMG_RAW></@IMG_RAW></@BASE64></@URLENCODE> to http://127.0.0.1/api/v1/ocr-captcha'

@app.route('/api/v1/ocr-captcha', methods=['POST'])
def image_to_text():
    """
    调用接口传来的图片内容，识别后返回api的响应
    """
    base64_img = request.form['image']
    if base64_img:
        image_name = save_to_image(base64_img)
        return ocr_image(image_name)
    else:
        return '获取图片失败'


# 获取的编码数据保存为图片
def save_to_image(base64_img):
    """
    将 base64 编码的图片数据保存为文件
    """
    bin_image = base64.b64decode(base64_img)
    image_name = '%s.png' % time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    # 数据保存到文件
    with open(image_name, 'wb') as f:
        f.write(bin_image)

    return image_name

def ocr_image(image_name):
    """
    使用 muggle_ocr 识别图片验证码
    """

    with open(image_name, 'rb') as f:
        captcha_bytes = f.read()

    # 初始化 model_type，选择 ModelType.Captcha ,识别验证码
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)

    for i in range(5):
        # 调用预测函数
        text = sdk.predict(image_bytes=captcha_bytes)
        return text

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True, port=8001, host='127.0.0.1')

