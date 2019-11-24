from django.shortcuts import get_object_or_404, render

from .models import Textbook


def index(request):
    latest_textbooks = Textbook.objects.order_by('pub_date')[:5]
    context = {'textbooks': latest_textbooks}
    return render(request, 'studb/index.html', context)

def textbook(request, textbook_id):
    textbook = get_object_or_404(Textbook, pk=textbook_id)
    return render(request, 'studb/textbook.html', {'textbook': textbook})