from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Car
import re
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django.http import JsonResponse
from .forms import FileForm
# Create your views here.
def signup(request):
    if request.method =="POST":
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username =user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Exists')
                return redirect('signup')
            user = User.objects.create_user(username = user_name,email= email, password = password1)
            user.save()
            return redirect('signin')
        else:
            messages.info(request,'Wrong Password')
            return redirect('signup')
    else:
        return render(request,'Cars/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username = username ,password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('signin')
    return render(request,'Cars/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def main(request):
    if Car.objects.filter(user=request.user):
                r = ['chevrolet chevelle malibu', 'ford galaxie 500', 'chevrolet impala', 'plymouth fury iii', 'pontiac catalina', 'buick estate wagon (sw)', 'plymouth duster', 'amc hornet', 'ford maverick', 'datsun pl510', 'peugeot 504', 'amc gremlin', 'toyota corona', 'ford pinto', 'amc matador', 'ford country squire (sw)', 
                'opel 1900', 'toyota corolla 1200', 'chevrolet vega', 'amc matador (sw)', 'ford gran torino (sw)', 'chevrolet malibu', 'ford gran torino', 'chevrolet caprice classic', 'ford ltd', 'plymouth valiant', 'fiat 128', 'opel manta', 'audi 100ls', 'saab 99le', 'toyota mark ii', 'chevrolet nova', 'chevrolet chevelle malibu classic', 'volkswagen dasher',
                'datsun 710', 'dodge colt', 'honda civic', 'subaru', 'buick century', 'toyota corolla', 'volkswagen rabbit', 'honda civic cvcc', 'chevrolet chevette', 'vw rabbit', 'buick skylark', 'chevrolet monte carlo landau', 'subaru dl', 'oldsmobile cutlass salon brougham', 'amc concord', 'dodge aspen', 'datsun 210', 'chevrolet citation', 'pontiac phoenix', 'mazda 626', 'honda accord', 'plymouth reliant']
                x_data = r
                y = []
                for i in r:
                    objects = Car.objects.filter(user=request.user,car_name=i)
                    summ = 0
                    cnt =0
                    for j in objects:
                        summ+=j.mpg
                        cnt+=1
                    y.append(summ/cnt)
                plt_div = plot([Scatter(x=x_data,y=y,mode='lines',name='test',opacity=0.8,marker_color='green')],output_type='div',include_plotlyjs=False)
                return render(request,'Cars/main.html',context={'plt_div':plt_div})
    return render(request,'Cars/main.html')
def save(request):
    if request.method == 'POST':
        fileform = FileForm(request.POST,request.FILES)
        if fileform.is_valid():
            print(1)
            file= fileform.cleaned_data["file"]
            lines = file.readlines()
            r= []
            for line in lines:
                line = line.decode('utf8')
                line = line.replace(" ","  ")
                line = line.replace("   ","  ")
                line = line.replace("      ","  ")
                line = line.replace("    ","  ")
                line = re.sub('\n',"",line)
                line = re.sub('\t','  ',line)
                line = line.split("  ")
                if '' in line:
                    line.remove('')
                s=''
                for j in line[8:]:
                    s+=j
                    s+=' '
                if line[3]=='?':
                    Car.objects.create(user=request.user,mpg=int(float(line[0])),cylinders=int(line[1]),displacement=int(float(line[2])),horsepower=int(float('0.0')),weight=int(float(line[4])),acceleration=int(float(line[5])),model_year=int(line[6]),origin=int(line[7]),car_name=s[1:len(s)-2])
                else:
                    Car.objects.create(user=request.user,mpg=int(float(line[0])),cylinders=int(line[1]),displacement=int(float(line[2])),horsepower=int(float(line[3])),weight=int(float(line[4])),acceleration=int(float(line[5])),model_year=int(line[6]),origin=int(line[7]),car_name=s[1:len(s)-2])
            if Car.objects.all():
                r = ['chevrolet chevelle malibu', 'ford galaxie 500', 'chevrolet impala', 'plymouth fury iii', 'pontiac catalina', 'buick estate wagon (sw)', 'plymouth duster', 'amc hornet', 'ford maverick', 'datsun pl510', 'peugeot 504', 'amc gremlin', 'toyota corona', 'ford pinto', 'amc matador', 'ford country squire (sw)', 
                'opel 1900', 'toyota corolla 1200', 'chevrolet vega', 'amc matador (sw)', 'ford gran torino (sw)', 'chevrolet malibu', 'ford gran torino', 'chevrolet caprice classic', 'ford ltd', 'plymouth valiant', 'fiat 128', 'opel manta', 'audi 100ls', 'saab 99le', 'toyota mark ii', 'chevrolet nova', 'chevrolet chevelle malibu classic', 'volkswagen dasher',
                'datsun 710', 'dodge colt', 'honda civic', 'subaru', 'buick century', 'toyota corolla', 'volkswagen rabbit', 'honda civic cvcc', 'chevrolet chevette', 'vw rabbit', 'buick skylark', 'chevrolet monte carlo landau', 'subaru dl', 'oldsmobile cutlass salon brougham', 'amc concord', 'dodge aspen', 'datsun 210', 'chevrolet citation', 'pontiac phoenix', 'mazda 626', 'honda accord', 'plymouth reliant']
                x_data = r
                y = []
                for i in r:
                    objects = Car.objects.filter(user=request.user,car_name=i)
                    summ = 0
                    cnt =0
                    for j in objects:
                        summ+=j.mpg
                        cnt+=1
                    y.append(summ/cnt)
                plt_div = plot([Scatter(x=x_data,y=y,mode='lines',name='test',opacity=0.8,marker_color='green')],output_type='div',include_plotlyjs=False)
                return JsonResponse({'status':'Save','plt_div':plt_div})
        
    if request.method =="GET":
        r = ['chevrolet chevelle malibu', 'ford galaxie 500', 'chevrolet impala', 'plymouth fury iii', 'pontiac catalina', 'buick estate wagon (sw)', 'plymouth duster', 'amc hornet', 'ford maverick', 'datsun pl510', 'peugeot 504', 'amc gremlin', 'toyota corona', 'ford pinto', 'amc matador', 'ford country squire (sw)', 
        'opel 1900', 'toyota corolla 1200', 'chevrolet vega', 'amc matador (sw)', 'ford gran torino (sw)', 'chevrolet malibu', 'ford gran torino', 'chevrolet caprice classic', 'ford ltd', 'plymouth valiant', 'fiat 128', 'opel manta', 'audi 100ls', 'saab 99le', 'toyota mark ii', 'chevrolet nova', 'chevrolet chevelle malibu classic', 'volkswagen dasher',
        'datsun 710', 'dodge colt', 'honda civic', 'subaru', 'buick century', 'toyota corolla', 'volkswagen rabbit', 'honda civic cvcc', 'chevrolet chevette', 'vw rabbit', 'buick skylark', 'chevrolet monte carlo landau', 'subaru dl', 'oldsmobile cutlass salon brougham', 'amc concord', 'dodge aspen', 'datsun 210', 'chevrolet citation', 'pontiac phoenix', 'mazda 626', 'honda accord', 'plymouth reliant']
        x_data = r
        data_to_Show = request.GET.get("show")
        print(data_to_Show)
        y = []
        if data_to_Show=="mpg":
            for i in r:
                objects = Car.objects.filter(car_name=i)
                summ = 0
                cnt =0
                for j in objects:
                    summ+=j.mpg
                    cnt+=1
                y.append(summ/cnt)
        else:
            for i in r:
                objects = Car.objects.filter(car_name=i)
                summ = 0
                cnt =0
                for j in objects:
                    summ+=j.weight
                    cnt+=1
                y.append(summ/cnt)
        
        plt_div = plot([Scatter(x=x_data,y=y,mode='lines',name='test',opacity=0.8,marker_color='green')],output_type='div',include_plotlyjs=False)
        return JsonResponse({'status':'Save','plt_div':plt_div})



