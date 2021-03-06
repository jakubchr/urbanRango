from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from rango.models import Category,Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

def _get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

#Helper functions
def visitor_cookie_handler(request):
    #get the number of visits to the site
    visits = int(_get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = _get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    most_viewed_category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'viewed_categories': most_viewed_category_list}
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'italicmessage': 'Jakub Charyton'}
    print(request.method)
    print(request.user)

    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug = category_name_slug.lower())

        pages = Page.objects.filter(category = category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return index(request)
        else:
            print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit = False)
                page.category = category
                page.views = 0
                page.user = request.user
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

@login_required
def logout_view(request):
    try:
        logout(request)
    except Exception as error:
        return HttpResponse("There was an error while logging out")
    else:
        return HttpResponseRedirect(reverse('rango:index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('rango:index'))
            else:
                return HttpResponse("Your account is inactive")
        else:
            return HttpResponse("Invalid login details: {0}".format(username))
        
    else:
        return render(request, 'rango/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("You're logged in so you can view this page")

