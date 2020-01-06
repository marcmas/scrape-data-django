import datetime

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import CertificateModelForm
from django.contrib.auth.models import User
from .models import Profile, Certificate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.template.loader import get_template, render_to_string
import pdfkit

# To render a pdf in iframe was used PDFKIT 
# pip install pdfkit and install "wkhtmltopdf" and add path 
def print_pdf(request, certificate_id):
    options = {
        'page-size': 'A4',
        'margin-top': '0.55in',
        'margin-right': '0.55in',
        'margin-bottom': '0.55in',
        'margin-left': '0.55in',
        'encoding': "UTF-8",
        # any other wkhtmltopdf options
    }

    results = get_object_or_404(Certificate, id=certificate_id)

    content = render_to_string(
        'certificate/pdf_certificate.html', {
            'cert': results
        }
    )
    print(results.leave_date)

    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/bin/wkhtmltopdf.exe')
    pdf = pdfkit.PDFKit(content, "string", options=options, configuration=config).to_pdf()

    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    pdf_name = str(results.leave_date) + "-" + results.user.first_name + "-" + str(results.leave_hour)
    # change attachment to atachment if you want open file in browser tab instead downloading
    response['Content-disposition'] = 'inline;filename={}.pdf'.format(pdf_name)

    return response


def download_pdf(request, certificate_id):
    options = {
        'page-size': 'A4',
        'margin-top': '0.55in',
        'margin-right': '0.55in',
        'margin-bottom': '0.55in',
        'margin-left': '0.55in',
        'encoding': "UTF-8",
        # any other wkhtmltopdf options
    }

    results = get_object_or_404(Certificate, id=certificate_id)

    content = render_to_string(
        'certificate/pdf_certificate.html', {
            'cert': results
        }
    )
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/bin/wkhtmltopdf.exe')
    pdf = pdfkit.PDFKit(content, "string", options=options, configuration=config).to_pdf()

    response = HttpResponse(pdf)
    response['Content-Type'] = 'application/pdf'
    pdf_name = str(results.leave_date) + "-" + results.user.first_name + "-" + str(results.leave_hour)

    # change attachment to attachment if you want open file in browser tab instead downloading
    response['Content-disposition'] = 'attachment;filename={}.pdf'.format(pdf_name)

    return response


@login_required(login_url="/")
def create(request):
    user = request.user
    form = CertificateModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = user
        form.save()
        return redirect('/certificate/lists/')
    
    context = {
        'form': form
    }

    return render(request, 'certificate/create.html', context)


def lists(request):
    all_certificate = Certificate.objects.order_by('-created_at').all()[:15]
    context = {
        'all_certificate': all_certificate
    }

    return render(request, 'certificate/lists.html', context)


def confirm_lists(request):
    all_certificate = Certificate.objects.filter(accept=True).all()[:15]
    context = {
        'all_certificate': all_certificate
    }

    return render(request, 'certificate/lists.html', context)


def cancle_lists(request):
    all_certificate = Certificate.objects.filter(accept=False).all()[:15]
    context = {
        'all_certificate': all_certificate
    }

    return render(request, 'certificate/lists.html', context)


def detail(request, certificate_id):
    unique_certificate = get_object_or_404(Certificate, id=certificate_id)
    context = {
        'unique_certificate': unique_certificate
    }

    return render(request, 'certificate/detail.html', context)


def delete(request, certificate_id):
    unique_certificate = get_object_or_404(Certificate, id=certificate_id)
    if unique_certificate.accept == True:
        messages.warning(request, 'The statement has been allready accepted. Cannot be removed')
        return redirect('/certificate/lists/')
    unique_certificate.delete()
    messages.warning(request, "The statement has been deleted")
    return redirect('/certificate/lists/')


@login_required(login_url="/")
def accept(request, certificate_id):
    unique_certif = get_object_or_404(Certificate, id=certificate_id)
    if unique_certif.accept == True:
        messages.warning(request, 'The statement has been allready accepted')
        return redirect('/certificate/lists/')
    unique_certif.accept = True
    unique_certif.save()
    if unique_certif.accept == True:
        messages.success(request, 'The statement has been accepted')
        return redirect('/certificate/lists/')
    else:
        messages.info(request, 'Has been some problems. Please try again.')
        return redirect('/certificate/lists/')
