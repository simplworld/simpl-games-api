
from collections import namedtuple
import os
import re

e_dict = {re.sub(r'^django_', '', k.lower()): v for k, v in os.environ.items() if k.startswith('DJANGO')}

e = namedtuple('django_env', e_dict.keys())(**e_dict)


