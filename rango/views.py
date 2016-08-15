from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Page
from .forms import CategoryForm, UserProfileForm, UserForm, PageForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.views.generic.edit import CreateView


def index(request):
    # request.session.set_test_cookie() #Test Cookie Code
    category_list = Category.objects.order_by('-likes')[:5]
    context = {'categories': category_list}
    return render(request, 'index.html', context)


def get_category(request, category_id=4):
    try:

        context_dict = {}
        category = Category.objects.get(id=category_id)
        page = Page.objects.filter(category=category)
        context_dict['pages'] = page  # page , pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)


def about(request):
    return render(request, 'about.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})


def add_page(request, page_id=4):
    try:
        cat = Category.objects.get(page_id)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=True)
                page.category = cat
                page.views = 0
                page.save()
                return get_category(request, page_id)
        else:
            print(form.errors)
    else:
        form = PageForm()
    context_dict = {'form': form, 'category': cat}
    return render(request, 'add_page.html', context_dict)

    # if request.method == 'POST':
    #     page_form = PageForm(request.POST)
    #     if page_form.is_valid():
    #         page_form.save(commit=True)
    #         return index(request)
    #     else:
    #         print(page_form.errors)
    # else:
    #     page_form = PageForm()

#    return render(request, 'add_page.html', {'page_form': page_form})


def register(request):
    # Test Cookie Code
    # if request.session.test_cookie_worked():
    #     print ('>>>TEST COOKIE Worked')
    #     request.session.delete_test_cookie()

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # if 'picture' in request.FILES:  # Install pillow , python3-dev
            #     profile.picture = request.FILES['picture']
            #     profile.save()
            #     registered = True
        else:
            print(user_form.errors, user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileForm()

    return render(request, 'register.html',
                  {'user_form': user_form,
                   'user_profile': user_profile,
                   'registered': registered})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("User Not Active Right Now...! ")
        else:
            print(
                "Invalid User Name Or password : {0}, {1}"
                .format(username, password))
            return HttpResponse("Invalid Login details.")
    else:
        return render(request, 'login.html', {})


@login_required
def restricted(request):
    return HttpResponse(
        "as long as you see this message So you are logged in :) شاطر"
    )


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')


# def track_url(request):
#     page_id = None
#     url = '/rango/'
#     if request.method == 'GET':
#         if 'page_id' in request.GET:
#             page_id = request.GET['page_id']
#             try:
#                 page = Page.objects.get(id=page_id)
#                 page.views = page.views+1
#                 page.save()
#                 url = page.url
#             except:
#                 pass
#     return redirect(url)
