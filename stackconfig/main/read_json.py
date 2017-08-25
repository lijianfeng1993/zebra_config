#!/usr/bin/env python
# coding = utf-8

import json

try:
    f = json.load(open('/root/zebra_config/examples/test.json'))
except IOError:
    js_data =None
else:
    js_data = f
    d = []
    for key in js_data:
        d.append(key)
