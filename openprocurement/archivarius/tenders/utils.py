# -*- coding: utf-8 -*-

from openprocurement.archivarius.core.utils import Root


def factory(request):
    root = Root(request)
    if not request.matchdict or not request.matchdict.get('tender_id'):
        return root
    request.validated['tender_id'] = request.matchdict['tender_id']
    tender = request.tender
    tender.__parent__ = root
    request.validated['tender'] = request.validated['db_doc'] = tender
    request.validated['tender_status'] = tender.status
    return tender
