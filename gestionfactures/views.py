import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.http import HttpResponse
from gestioncommandes.models import Commande
from datetime import datetime


# Create your views here.
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def generate_facture(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    params = {"commande": commande, "dateNow": datetime.now()}
    template = get_template("gestionfactures/pdf.html")
    html = template.render(params)
    response = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
    response.seek(0)
    if not pdf.err:
        return FileResponse(response, as_attachment=True, filename='facture'+str(commande.id)+str(commande.client)+str(commande.personnel)+'.pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
