# coding=utf-8
import os

from .cookies_cache import SDUT, create_db, db_name
from .dormitory import Dormitory
from .ecard import Ecard
from .ehall import Ehall
from .lib import Lib
from .logistics import Logistics
from .meol import Meol

if not os.path.exists(db_name):
    create_db()
