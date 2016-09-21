# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm


def list(request):
    if not request.user.is_authenticated:
        # return redirect('/myapp')
        
        return render(
            request,
            'list.html',
            {'current_user':request.user,'documents': [], 'form': []}
        )
        
 
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.order_by('f01')[:100]

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'current_user':request.user,'documents': documents, 'form': form}
    )

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    #return redirect('/admin/login/?next=/app001')        
    # 2016-08-24
    # When log out, got to root 
    return redirect('/myapp/list')  