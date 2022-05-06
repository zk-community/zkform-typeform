#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>
# Airtable Interface for ZKDB (Zero Knowledge Podcast DB)
__app_name__ = "zkform"
__version__ = "0.1"
'''
0.1: 
'''

from typeform import Typeform

import pandas as pd

from datetime import datetime
TODAY = datetime.today().date()

import json
import os
import re
import logging
log_format = '>> %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
log = logging.getLogger()

#import requests
#req_log = requests.logging.getLogger()
#req_log.setLevel(logging.WARNING)  # Quiet down request API calls to airtable

config_file = '/home/bitnami/notebooks/.env'
with open(config_file) as cf:
    config = json.load(cf)

class ZKForm:
    def __init__(self):
        self.config = self._load_config()
        self.api_key = self.config["TYPEFORM_API_KEY"]
        self.api = Typeform(self.api_key)
        self._cache_load()

    def _cache_load(self):
        log.info('Loading Data Cache ...')
        self.forms: dict = self.api.forms.list()
        self.responses = self.api.responses
        log.info('Done.')
        return True

    def _load_config(self, env_path='.env'):
        env_path = env_path or '.env'
        config = {}
        if os.path.exists(env_path):
            with open(env_path) as env_conf:
                config = json.load(env_conf)
        return config

    def get_lists(self):
        return self. forms

    def get_responses(self, list_id):
        _r = self.responses.list(list_id)
        return _r

#    def something():
#        df_items = pd.DataFrame(result['items'])
#        df_items['meta_list_id'] = list_id
#        df_items['meta_page_count'] = result['page_count']
#        df_items['meta_total_items'] = result['total_items']
#        answers = df_items['answers']
#        for a in answers:
#            for field in a:
#                ftype = field['type']
#                fvar = field[ftype]
#                print(ftype, fvar)
#        for a in answers:
#            for field in a:
#                print (field['field'])

if __name__ == "__main__":
    zform = ZKForm()
