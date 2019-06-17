from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.views.generic import ListView, DetailView

from posts.forms import PostForm
from posts.mixins import PostCreateRequiredMixin
from posts.models import Post


class PostListCreateView(PostCreateRequiredMixin, ListView):
    template_name = 'post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        if self.request.resolver_match.url_name == 'roundup_list':
            code = 'roundup'
        else:
            code = 'blog'
        paginator = Paginator(Post.objects.filter(category__category_code=code).order_by('-created'), 7)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        # Add post_form into context for preparing the post form.
        # Only for GET method
        context = super(PostListCreateView, self).get_context_data(**kwargs)
        f = PostForm()
        print(self.request.resolver_match)
        if self.request.resolver_match.url_name == 'roundup_list':
            f.fields['category'].initial = 1
        else:
            f.fields['category'].initial = 2
        context['post_form'] = f
        return context

    def post(self, request, *args, **kwargs):
        # Handle POST for creating a post
        f = PostForm(request.POST)
        if f.is_valid():
            new_post = f.save(commit=False)
            new_post.user = request.user
            new_post.save()
            f.clean()
            new_post.clean()
            f = PostForm()
        request.POST = None
        return HttpResponseRedirect(reverse(self.request.resolver_match.url_name))


class PostDetailUpdateView(DetailView):
    template_name = 'post.html'

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs['slug'])

