""" Download image according to given urls and automatically rename them in order. """
# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

from __future__ import print_function
import logging
import shutil
import imghdr
import os
import concurrent.futures
import requests
import io
from tkinter import *
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, sdch",
    # 'Connection': 'close',
}


def download_image(logger,image_url, dst_dir, file_name, timeout=20, proxy_type=None, proxy=None):
    proxies = None
    if proxy_type is not None:
        proxies = {
            "http": proxy_type + "://" + proxy,
            "https": proxy_type + "://" + proxy
        }

    response = None
    file_path = os.path.join(dst_dir, file_name)
    try_times = 0
    while True:
        try:
            try_times += 1
            response = requests.get(
                image_url, headers=headers, timeout=timeout, proxies=proxies)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            response.close()
            file_type = imghdr.what(file_path)
            # if file_type is not None:
            if file_type in ["jpg", "jpeg", "png", "bmp"]:
                new_file_name = "{}.{}".format(file_name, file_type)
                new_file_path = os.path.join(dst_dir, new_file_name)
                shutil.move(file_path, new_file_path)
                logger.log(logging.INFO,"## OK:  {}  {}\n".format(new_file_name, image_url))
                # print("## OK:  {}  {}".format(new_file_name, image_url))
            else:
                os.remove(file_path)
                # print("## Err:  {}".format(image_url))
                logger.log(logging.ERROR,"## Err:  {}\n".format(image_url))
            break
        except Exception as e:
            if try_times < 3:
                continue
            if response:
                response.close()
            # print("## Fail:  {}  {}".format(image_url, e.args))
            logger.log(logging.ERROR, "## Fail:  {}  {}\n".format(image_url, e.args))

            break


def download_images(logger,image_urls, dst_dir, file_prefix="img", concurrency=50, timeout=20, proxy_type=None, proxy=None,classname='',keyword=''):
    """
    Download image according to given urls and automatically rename them in order.
    :param timeout:
    :param proxy:
    :param proxy_type:
    :param image_urls: list of image urls
    :param dst_dir: output the downloaded images to dst_dir
    :param file_prefix: if set to "img", files will be in format "img_xxx.jpg"
    :param concurrency: number of requests process simultaneously
    :param keyword: keyword for save
    :return: none
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        future_list = list()
        count = 0
        new_desdir=dst_dir+'/'+classname+'/'+keyword
        if not os.path.exists(new_desdir):
            os.makedirs(new_desdir)
            pasturldownload=[]
        else:
            fname=new_desdir+'/'+keyword+'.txt'
            pasturldownload = []
            if os.path.isfile(fname) :
                filleepast=open(fname,'r')
                for line in filleepast:
                    mm=line.split('\t')
                    pasturldownload.append(mm[1].strip().rstrip())
                    count = mm[0].split('_')
                    count = int(count[1])
            else:
                pasturldownload = []
        with io.open(new_desdir+'/'+keyword+'.txt','a+') as filee:
            for image_url in image_urls:
                if image_url not in pasturldownload:
                    file_name = file_prefix + "_" + "%04d" % count
                    future_list.append(executor.submit(
                    download_image,logger, image_url, new_desdir, file_name, timeout, proxy_type, proxy))
                    count += 1
                    filee.write(file_name+'\t'+image_url+'\n')
                    filee.flush()
        concurrent.futures.wait(future_list, timeout=180)
