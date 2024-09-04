from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .utils import get_mongodb
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag


# Create your views here.
def main(request, page=1):
    # mongo setup
    # db = get_mongodb()
    # quotes = db.quotes.find()

    # postgres setup
    quotes = Quote.objects.all()  # Fetch quotes from PostgresSQL

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
            # Get the selected author
            author_id = request.POST.get('author')
            selected_author = Author.objects.get(id=author_id)
            # Save the quote with the selected author
            new_quote = form.save(commit=False)
            new_quote.author = selected_author
            new_quote.save()

            # choice_authors = Author.objects.filter(fullname__in=request.POST.getlist('authors'))

            # for an_author in choice_authors.iterator():
            #     new_quote.author = an_author

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/quote.html', {'authors': authors, 'form': form})

    return render(request, 'quotes/quote.html', {'authors': authors, 'form': QuoteForm()})


def author_about(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author_about.html', {'author': author})


def tags(request, tag_name, page=1):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    quotes_per_page = 10
    paginator = Paginator(quotes, quotes_per_page)
    quotes_displayed_on_page = paginator.page(page)

    return render(request, 'quotes/tags.html', {
        'tag_name': tag_name,
        'quotes': quotes_displayed_on_page,
    })