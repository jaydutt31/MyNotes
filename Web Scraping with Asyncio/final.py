import os
import asyncio 
from arsenic import get_session, keys, browsers, services
import pandas as pd 
from requests_html import HTML 
import itertools
import re, time, pathlib
from urllib.parse import urlparse

import loggin 
import structlog