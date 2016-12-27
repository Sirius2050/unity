# coding=utf-8
import base64
import random
import requests
import json
import logging

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        try:
            r = requests.get('http://101.200.55.192:8000/?type=1&count=20')
            #logging.info('contents:%s' % contents.text)
            data = json.loads(r.text)
            if len(data) > 0:
                proxy = random.choice(data)
                ip = proxy.get('ip')
                port = proxy.get('port')
                address = '%s:%s' % (ip, port)

                request.meta['proxy'] = 'http://%s' % address
                logging.info('********ProxyMiddleware proxy*******:%s' % request.meta['proxy'] )
        except Exception, e:
            logging.warning('ProxyMiddleware Exception:%s' % str(e))
