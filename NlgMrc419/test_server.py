# -*- coding:utf8 -*-
# ==============================================================================
# open
# ==============================================================================
"""
This module tests the mrc http web service api.
"""
#import urllib2
import urllib2
import json
import time
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf8')

url = "http://yq01-gpu-86-74-18-00.xxx.xxx.com:8000/spo"

data = {"s": "广汽传祺gs4", "p": "车体结构", 'para': "传祺GS42015款200TG-DCT精英版车体结构为\
        承载式，了解更多传祺GS42015款200TG-DCT精英版车体结构就来汽车江湖网参数明细频道。"}
start = time.time()
post_data = json.dumps(data)
req = urllib2.Request(url)
response = urllib2.urlopen(req, post_data)
content = response.read()
ans = json.loads(content)
for k, v in ans.items():
    print ('k: {}, v: {}'.format(k, v))
end = time.time()
print ('time: {}'.format(end - start))

