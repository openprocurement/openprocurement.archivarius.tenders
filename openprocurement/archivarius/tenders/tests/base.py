# -*- coding: utf-8 -*-
import os
from openprocurement.tender.belowthreshold.tests.base import TenderContentWebTest


class BaseTenderArchivariusWebTest(TenderContentWebTest):
    relative_to = os.path.dirname(__file__)
