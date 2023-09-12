from django.shortcuts import render, get_object_or_404
from app.models import Post
from django.core.paginator import Paginator
from app.forms import UserSearchForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(is_activate=True)

    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'index.html', context=context)

def post(request):
        form = UserSearchForm(request.POST)
        search_query = request.GET.get("search", "")
        filter1 = request.GET.get('city_filter')
        print(search_query)
        print(filter1)

        if filter1 == "ALL" or search_query == "":
            if filter1 != "ALL":
                post = Post.objects.filter(city=filter1)
            if search_query != "":
                post = Post.objects.filter(search_query=search_query)
            if filter1 == "ALL" and search_query == "":
                post = Post.objects.all
        elif filter1 == None and search_query == "":
            post = Post.objects.all
        elif filter1 != "ALL" and search_query != "":
            post = Post.objects.filter(city=filter1)
            
        paginator = Paginator(post, 5)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'form': form,
        }

        return render(request, 'post/index.html', context=context)

def post_details(request, pk):
      post = get_object_or_404(Post, pk=pk)

      return render(request, "post/post_details.html", {'post': post})
