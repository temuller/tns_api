# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()
try:
    TNS_BOT_ID = os.getenv("tns_bot_id")
except:
    TNS_BOT_ID = os.getenv("tns_id")  # old version
try:
    TNS_BOT_NAME = os.getenv("tns_bot_name")
except:
    TNS_BOT_NAME = os.getenv("name")  # old version
try:
    TNS_API_KEY = os.getenv("tns_api_key")
except:
    TNS_API_KEY = os.getenv("api_key")  # old version