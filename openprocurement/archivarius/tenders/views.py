# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.archivarius.core.utils import ArchivariusResource
from openprocurement.archivarius.tenders.utils import factory


@opresource(name='Tender Archivarius',
            path='/tenders/{tender_id}/dump',
            description="Tender Archivarius View",
            factory=factory)
class TenderArchivariusResource(ArchivariusResource):

    pass
