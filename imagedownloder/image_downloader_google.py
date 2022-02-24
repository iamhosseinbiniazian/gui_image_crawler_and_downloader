# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:37:17 2018

@author: apasai
"""

# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

from __future__ import print_function

import argparse

import crawler
import downloader
import sys
def main(argv,classname,keyword):
    parser = argparse.ArgumentParser(description="Image Downloader")
    # parser.add_argument("keywords", type=str,
    #                     help='Keywords to search. ("in quotes")')
    parser.add_argument("--engine", "-e", type=str, default="Google",
                        help="Image search engine.", choices=["Google", "Bing", "Baidu"])
    parser.add_argument("--max-number", "-n", type=int, default=-4,
                        help="Max number of images download for the keywords.")
    parser.add_argument("--num-threads", "-j", type=int, default=50,
                        help="Number of threads to concurrently download images.")
    parser.add_argument("--timeout", "-t", type=int, default=20,
                        help="Seconds to timeout when download an image.")
    parser.add_argument("--output", "-o", type=str, default="./download_imagess",
                        help="Output directory to save downloaded images.")
    parser.add_argument("--safe-mode", "-S", action="store_true", default=False,
                        help="Turn on safe search mode.")
    parser.add_argument("--face-only", "-F", action="store_true", default=False,
                        help="Only search for ")
    parser.add_argument("--proxy_http", "-ph", type=str, default=None,
                        help="Set http proxy (e.g. 192.168.0.2:8080)")
    parser.add_argument("--proxy_socks5", "-ps", type=str, default=None,
                        help="Set socks5 proxy (e.g. 192.168.0.2:1080)")
    parser.add_argument("--numImage", type=int, default=200,
                        help="Number of Image to Download")

    args = parser.parse_args(args=argv)

    proxy_type = None
    proxy = None
    if args.proxy_http is not None:
        proxy_type = "http"
        proxy = args.proxy_http
    elif args.proxy_socks5 is not None:
        proxy_type = "socks5"
        proxy = args.proxy_socks5
    numImage=args.numImage
    crawled_urls = crawler.crawl_image_urls(keyword,
                                            engine=args.engine, max_number=args.max_number,
                                            face_only=args.face_only, safe_mode=args.safe_mode,
                                            proxy_type=proxy_type, proxy=proxy,
                                            browser="chrome",numImage=numImage)
    downloader.download_images(image_urls=crawled_urls, dst_dir=args.output,
                               concurrency=args.num_threads, timeout=args.timeout,
                               proxy_type=proxy_type, proxy=proxy,
                               file_prefix=args.engine,classname=classname,keyword=keyword)

    print("Finished.")


if __name__ == '__main__':
    import io
    from xlrd import open_workbook
    import csv
    templist=[]
    tags=[]
    with io.open('Tag.csv',encoding='utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            templist=[]
            templist.append(row[0].strip().rstrip())
            templist.append(row[1].strip().rstrip())
            tags.append(templist)
    # book = open_workbook('Tag.xlsx')
    # sheet = book.sheet_by_index(0)

    # for row in range(0, sheet.nrows):
    #     templist=[]
    #     templist.append(sheet.cell_value(row,0).strip().rstrip())
    #     templist.append(sheet.cell_value(row,1).strip().rstrip())
    #     tags.append(templist)

    # tags=[['علی' ,'قلی'],['علی' ,'ذوالفقار'],['بدحجابی' ,'نمایانی موی سر']]
    with io.open('OK.txt', 'r',encoding='utf8') as f:
        lines = f.readlines()
    tagok=list()
    for line in lines:
        ll=line.strip().rstrip()
        if ll!='':
            tagok.append(ll)
    finaltag=[x for x in tags if x[1] not in tagok]
    print(finaltag)
    with io.open('OK.txt','a+',encoding='utf8') as fff:
        for keyword in finaltag:
            try:
                main(sys.argv[1:],keyword[0],keyword[1])
                fff.write(keyword[1]+'\n')
                fff.flush()
            except:
                print('Not Crawled:',keyword[1])

