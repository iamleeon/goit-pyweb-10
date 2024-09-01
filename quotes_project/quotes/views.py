from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb


# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    quotes_per_page = 10
    paginator = Paginator(list(quotes), quotes_per_page)
    quotes_displayed_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_displayed_on_page })
