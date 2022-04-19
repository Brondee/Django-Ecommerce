from django.shortcuts import render

from main.services import search_function, paginator_for_page_function

# Create your views here.
def search(response):
    if response.method == "GET":

        query = response.GET.get('q')

        search_results = search_function(query)

        paginate = paginator_for_page_function(response, search_results[1])

        return render(response, "search/search.html", {"query": query, "products": paginate[0], "pages": paginate[1], "search_success":search_results[0],})