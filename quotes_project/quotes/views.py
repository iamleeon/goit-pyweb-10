from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Author


# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    quotes_per_page = 10
    paginator = Paginator(list(quotes), quotes_per_page)
    quotes_displayed_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_displayed_on_page})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})


def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_authors = Author.objects.filter(fullname__in=request.POST.getlist('authors'))

            for an_author in choice_authors.iterator():
                new_quote.author = an_author

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/quote.html', {'authors': authors, 'form': form})

    return render(request, 'quotes/quote.html', {'authors': authors, 'form': QuoteForm()})
