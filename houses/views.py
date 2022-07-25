from django.shortcuts import render,redirect
from .models import Agent,Amenity,House,Blog,Comment,AgentAccount,Message,Image_of_house
from .forms import CommentForm,HouseForm,BlogForm,AgentForm
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse,reverse_lazy
# Create your views here.
def index(request):
    if request.method=="POST":
        print("FOOOOOOOOOOOOOOOOOOORM")
        print(request.POST)
        pass
    all_houses = House.objects.all()[:3]
    all_agents = Agent.objects.all()[:3]
    all_blogs = Blog.objects.all()[:3]
    context = {"all_houses": all_houses,
               "all_agents":all_agents,
               "all_blogs":all_blogs}
    return render(request,"houses/index.html",context)

def single(request,id):
    single_house = House.objects.get(id=id)
    if request.method=="POST":
        print("##########################")
        print(request.POST)
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        new_msg = Message(user_name=name,content=message,email=email,agent=single_house.agent)
        new_msg.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    context = {"house":single_house}
    return render(request,"houses/property-single.html",context)

"""
def properties(request):
    all_houses = House.objects.all()
    context = {"all_houses":all_houses}
    return render(request,"houses/property-grid.html",context)
"""
#######################
class propertiesView(ListView):
    model = House
    paginate_by = 6
    template_name = "houses/property-grid.html"
    context_object_name = "all_houses"
####################
def about(request):
    return render(request,"houses/about.html")

def agent(request,id):
    single_agent = Agent.objects.get(id=id)
    if request.method == "POST":
        print("##########################")
        print(request.POST)
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        new_msg = Message(user_name=name, content=message, email=email, agent=single_agent)
        new_msg.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    context = {"agent":single_agent}
    return render(request,"houses/agent-single.html",context)
"""
def agents(request):
    all_agents = Agent.objects.all()
    context = {"all_agents":all_agents}
    return render(request,"houses/agents-grid.html",context)
"""
##############################
class agentsView(ListView):
    model = Agent
    paginate_by = 3
    template_name = "houses/agents-grid.html"
    context_object_name = "all_agents"
##############################

def blog(request,id):
    form = CommentForm()
    if request.method=="POST":
        form = CommentForm(request.POST, request.FILES)
        print("#################")
        print(request.POST)
        if form.is_valid():
            add_blog = form.save(commit=False)
            add_blog.blog = Blog.objects.get(id=id)
            add_blog.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    single_blog = Blog.objects.get(id=id)
    context = {"blog":single_blog,
               "form":form}
    return render(request,"houses/blog-single.html",context)
"""
def blogs(request):
    all_blogs = Blog.objects.all()
    context = {"all_blogs":all_blogs}
    return render(request,"houses/blog-grid.html",context)
"""
##############################
class blogsView(ListView):
    model = Blog
    paginate_by = 3
    template_name = "houses/blog-grid.html"
    context_object_name = "all_blogs"
################################
"""
def search_me(request):
    print("search me #####################")
    print(request.POST)
    city = request.POST["city"]
    bedrooms = request.POST["bedrooms"]
    garages = request.POST["garages"]
    bathrooms = request.POST["bathrooms"]
    price = request.POST["price"]
    all_houses = House.objects.filter(Q(location__icontains=city),
                                      Q(beds__gte=bedrooms),
                                      Q(garages__gte=garages),
                                      Q(bathrooms__gte=bathrooms),
                                      Q(price__gte=price))
    print("number of search houses ============")
    print(all_houses.count())
    context = {"all_houses":all_houses}
    return render(request,"houses/search_results.html",context)
"""
#################
class search_meView(ListView):
    model = House
    paginate_by = 3
    template_name = "houses/search_results.html"
    context_object_name = "all_houses"
    def get_queryset(self):
        print("########################")
        print(self.request.GET)
        base_query = super().get_queryset()
        city = self.request.GET["city"]
        bedrooms = self.request.GET["bedrooms"]
        garages = self.request.GET["garages"]
        bathrooms = self.request.GET["bathrooms"]
        price = self.request.GET["price"]
        if city or bedrooms or garages or bathrooms or price:
            data = base_query.filter(Q(location__icontains=city),
                                              Q(beds__gte=bedrooms),
                                              Q(garages__gte=garages),
                                              Q(bathrooms__gte=bathrooms),
                                              Q(price__gte=price))
        else:
            data = base_query
        return data
#################################

def userlogin(request):
    prev_link = request.GET["next"]
    print("++++++++++++++++++")
    print(prev_link)
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(prev_link)
        else:
            pass
    return render(request,"houses/login.html")

def userregister(request):
    form = UserCreationForm()
    if request.method=="POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        form = UserCreationForm(request.POST)
        form.username = username
        form.password1 = password1
        form.password2 = password2
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    context = {"form":form}
    return render(request,"houses/register.html",context)

def userlogout(request):
    logout(request)
    return redirect('home')

def Profile(request):
    user = request.user
    agent_user = AgentAccount.objects.get(user=user)
    context = {"agent_user":agent_user,
               "agent":agent_user.agent}
    return render(request,"houses/profile.html",context)

def messages(request):
    user = request.user
    agent_user = AgentAccount.objects.get(user=user)
    context = {"agent_user": agent_user,
               "agent": agent_user.agent}
    return render(request, "houses/messages.html", context)

def add_house(request):
    form = HouseForm()
    if request.method == "POST":
        list = []  # files is the key of a multi value dictionary, values are the uploaded files
        for f in request.FILES.getlist('files'):  # files is the name of your html file button
            filename = f.name
            list.append(filename)
        print("0000000000000000000000")
        print(list)
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            house = House.objects.all()[House.objects.all().count()-1]
            for other_img in list:
                new_img = Image_of_house(img="images/"+other_img,house=house)
                new_img.save()
            return redirect('properties')
    context = {"form":form}
    return render(request,"houses/add_house.html",context)

def add_blog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    context = {"form":form}
    return render(request,"houses/add_house.html",context)

def add_agent(request):
    form = AgentForm()
    if request.method == "POST":
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agents')
    context = {"form":form}
    return render(request,"houses/add_house.html",context)

class update_agent(UpdateView):
    model = Agent
    fields = "__all__"
    template_name = "houses/update_agent.html"
    def get_success_url(self):
        my_agent = self.object
        print("#######################")
        print(self.object)
        print(self.request)
        return reverse("agent",args=[my_agent.id])

class update_blog(UpdateView):
    model = Blog
    fields = "__all__"
    template_name = "houses/update_agent.html"
    def get_success_url(self):
        my_blog = self.object
        print("#######################")
        print(self.object)
        print(self.request)
        return reverse("blog",args=[my_blog.id])

class update_property(UpdateView):
    model = House
    fields = "__all__"
    template_name = "houses/update_agent.html"
    def get_success_url(self):
        my_property = self.object
        print("#######################")
        print(self.object)
        print(self.request)
        return reverse("single",args=[my_property.id])

class delete_agent(DeleteView):
    model = Agent
    success_url = reverse_lazy('agents')

class delete_blog(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')

class delete_property(DeleteView):
    model = House
    success_url = reverse_lazy('properties')