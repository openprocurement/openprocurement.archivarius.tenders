# -*- coding: utf-8 -*-
import os
from openprocurement.api.tests.base import BaseTenderWebTest


class BaseTenderArchivariusWebTest(BaseTenderWebTest):
    relative_to = os.path.dirname(__file__)
