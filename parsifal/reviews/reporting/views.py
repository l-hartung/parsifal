# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse as r
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import SuspiciousOperation

from parsifal.reviews.models import *
from parsifal.reviews.decorators import author_required
from parsifal.reviews.reporting.export import export_review_to_docx, export_review_to_json


@author_required
@login_required
def reporting(request, username, review_name):
    return redirect(r('export', args=(username, review_name,)))

@author_required
@login_required
def export(request, username, review_name):
    review = get_object_or_404(Review, name=review_name, author__username__iexact=username)
    return render(request, 'reporting/export.html', { 'review': review })

@author_required
@login_required
def download(request):
    export_format=request.GET.get('export-format')
    if export_format=='docx':
        return download_docx(request)
    elif export_format=='json':
        return download_json(request)
    else:
        raise SuspiciousOperation()


@author_required
@login_required
def download_docx(request):
    review_id = request.GET.get('review-id')
    review = get_object_or_404(Review, pk=review_id)
    sections = request.GET.getlist('export')
    document = export_review_to_docx(review, sections)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = u'attachment; filename={0}.docx'.format(review.name)
    document.save(response)
    return response


@author_required
@login_required
def download_json(request):
    review_id = request.GET.get('review-id')
    review = get_object_or_404(Review, pk=review_id)
    sections = request.GET.getlist('export')
    json_document = export_review_to_json(review, sections)
    response = HttpResponse(json_document, content_type='application/json')
    response['Content-Disposition'] = u'attachment; filename={0}.json'.format(review.name)
    #document.save(response)
    return response
