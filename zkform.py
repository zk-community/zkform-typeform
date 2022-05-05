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

TYPEFORM_API_KEY = config.get('TYPEFORM_API_KEY', '')

tf = Typeform(TYPEFORM_API_KEY)
forms: dict = tf.forms.list()
#tf.forms.get('eOCXPfIy')

class ZKForm:
    def __init__(self):
        self.config = self._load_config()

        self.api_key = self.config["TYPEFORM_API_KEY"]

        self.api = TypeForm(self.api_key)

        self._cache_load()

    def _cache_load(self):
        log.info('Loading Data Cache ...')
        log.info('Done.')
        return tables

    def _load_config(self, env_path='.env'):
        env_path = env_path or '.env'
        config = {}
        if os.path.exists(env_path):
            with open(env_path) as env_conf:
                config = json.load(env_conf)
        return config


if __name__ == "__main__":
    zkform = ZKForm()
