from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from random import *
from accounts.models import *
from game.models import *
from accounts import forms
from accounts.viewbag import view_bag
from game.views import *

my_bag = view_bag()

def login(request):
    form = forms.FormLogin()
    connect = False
    if request.POST:
        username = request.POST['UserName']
        password = request.POST['Password']

        for user in Account.objects.values():
            if user['username'] == username and user['password'] == password:
                connect = True
                my_bag.set('user', user)
                break
        if not connect:
            return render(request, 'accounts/login.html', {'form':form, 'error_message':'invalid username or password'})
        else:
            if user['role'] == 'Kindergarden':
                my_bag.set('institution',user['institution'])
                my_bag.set('teacher',user)
                form1 = forms.ChildForm()
                return render(request, 'accounts/institutions.html', {'user': user, 'form': form1, 'institution_name':my_bag.get('institution'), 'accounts': Account.objects.values(), 'teacher_details':my_bag.get('teacher')})
            elif user['role'] == 'Child':
                return render(request, 'accounts/games.html', {'user': user, 'games': listed_games(my_bag.get('user')['categories'].keys())})
            elif user['role'] == 'Administrator':
                form1 = forms.KindergardenForm()
                return render(request, 'accounts/admin_dashboard.html', {'form': form1, 'user': user, 'accounts': Account.objects.values('institution').distinct()})
    
    return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})


def admin_dashboard(request):
    try:
        form = forms.KindergardenForm()
        # for user in Account.objects.values():
        #         if user['username'] == 'admin':
        #             break
        if request.POST:
            firstname_ = request.POST['FirstName']
            lastname_ = request.POST['LastName']
            username_ = request.POST['UserName']
            password_ = request.POST['Password']
            institution_ = request.POST['Institution']
            if {'institution': institution_} in Account.objects.values('institution').distinct():
                return render(request, 'accounts/admin_dashboard.html', {'form': form, 'user':my_bag.get('user'), 'accounts': Account.objects.values('institution').distinct(), 'errorMessage': 'Institution is already exists!'})
            else: 
                import os
                import django
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
                django.setup()
                try:
                    usr = Account.objects.get_or_create(first_name=firstname_, last_name=lastname_, username=username_, password=password_, institution=institution_, role=form.get_role())[0]
                    usr.save()
                except:
                    return render(request, 'accounts/admin_dashboard.html', {'form': form, 'user':my_bag.get('user'), 'accounts': Account.objects.values('institution').distinct(), 'errorMessage': 'Username is already exists!'})

        return render(request, 'accounts/admin_dashboard.html', {'form': form, 'user':my_bag.get('user'), 'accounts': Account.objects.values('institution').distinct()})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def logout(request):
    try:
        my_bag.clear()
        form = forms.FormLogin()
        return render(request, 'accounts/login.html', {'form':form, 'error_message': ''})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def institutions(request):
    try:
        if request.GET:
            my_bag.set('institution', request.GET['institution'])
            for teacher_details in Account.objects.values():
                    if teacher_details['institution'] == request.GET['institution'] and teacher_details['role'] == 'Kindergarden':
                        my_bag.set('teacher', teacher_details)
                        break
        form = forms.ChildForm()
        if request.POST:
            firstname_ = request.POST['FirstName']
            lastname_ = request.POST['LastName']
            username_ = request.POST['UserName']
            password_ = request.POST['Password']
            categories_ = {}

            if my_bag.get('user')['role'] == 'Kindergarden':
                all_categories = my_bag.get('user')['categories']
            else:
                all_categories = my_bag.get('techer')['categories']
            for category in all_categories.values():
                categories_[category] = "0"

            import os
            import django
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
            django.setup()
            try:
                usr = Account.objects.get_or_create(categories = categories_, first_name=firstname_, last_name=lastname_, username=username_, password=password_, institution=my_bag.get('teacher')['institution'], role=form.get_role(), rating = form.get_rating())[0]
                usr.save()
            except:
                print("\n\n\n", username_, "\n\n\n")
                return render(request, 'accounts/institutions.html', {'form':form, 'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'accounts': Account.objects.values(), 'teacher_details':my_bag.get('teacher'), 'errorMessage': 'Username is already exists!'})
        return render(request, 'accounts/institutions.html', {'form':form, 'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'accounts': Account.objects.values(), 'teacher_details':my_bag.get('teacher')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def child(request):
    try:
        if request.GET:
            for child_details in Account.objects.values():
                    if child_details['username'] == request.GET['child']:
                        my_bag.set('child', child_details)
                        break
        form = forms.ChildEditForm(initial = {'UserName': my_bag.get('child')['username'], 'Password': my_bag.get('child')['password'], 'FirstName': my_bag.get('child')['first_name'], 'LastName': my_bag.get('child')['last_name'], 'rating': my_bag.get('child')['rating'], 'Institution': my_bag.get('child')['institution']})
        if request.POST:
            firstname_ = request.POST['FirstName']
            lastname_ = request.POST['LastName']
            username_ = request.POST['UserName']
            password_ = request.POST['Password']
            institution_ = request.POST['Institution']
            rating_ = request.POST['rating']
            import os
            import django
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
            django.setup()
            usr = Account.objects.get(username=my_bag.get('child')['username'])
            usr.username = username_
            usr.first_name = firstname_
            usr.last_name = lastname_
            usr.password = password_
            usr.institution = institution_
            usr.rating = rating_
            usr.save()
            for child_details in Account.objects.values():
                    if child_details['username'] == username_:
                        my_bag.set('child', child_details)
                        break
            form = forms.ChildEditForm(initial = {'UserName': my_bag.get('child')['username'], 'Password': my_bag.get('child')['password'], 'FirstName': my_bag.get('child')['first_name'], 'LastName': my_bag.get('child')['last_name'], 'rating': my_bag.get('child')['rating'], 'Institution': my_bag.get('child')['institution']})


        return render(request, 'accounts/child.html', {'form':form, 'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'child_details': my_bag.get('child')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def teacher_dashboard(request):
    try:
        return render(request, 'accounts/teacher_dashboard.html', {'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def my_class(request):
    try:
        return render(request, 'accounts/my_class.html', {'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def teacher_details(request):
    try:
        form = forms.KindergardenForm(initial = {'UserName': my_bag.get('teacher')['username'], 'Password': my_bag.get('teacher')['password'], 'FirstName': my_bag.get('teacher')['first_name'], 'LastName': my_bag.get('teacher')['last_name'], 'Institution': my_bag.get('teacher')['institution']})

        # form = forms.KindergardenForm()
        if request.GET:
            print('get\n')
        elif request.POST:
            firstname_ = request.POST['FirstName']
            lastname_ = request.POST['LastName']
            username_ = request.POST['UserName']
            password_ = request.POST['Password']
            institution_ = request.POST['Institution']
            old_institution = my_bag.get('institution')
            import os
            import django
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
            django.setup()
            # for usr in Account.objects.values():
            #     if usr['username'] == my_bag.get('teacher')['username']:
            #         break
            usr = Account.objects.get(username=my_bag.get('teacher')['username'])
            usr.username = username_
            usr.first_name = firstname_
            usr.last_name = lastname_
            usr.password = password_
            usr.institution = institution_
            usr.save()
            for teacher_details in Account.objects.values():
                    if teacher_details['username'] == username_:
                        my_bag.set('teacher', teacher_details)
                        my_bag.set('institution', my_bag.get('teacher')['institution'])
                        break
            if my_bag.get('institution') != old_institution:
                for child in Account.objects.values():
                    if child['institution'] == old_institution:
                        usr = Account.objects.get(username=child['username'])
                        usr.institution = institution_
                        usr.save()
            form = forms.KindergardenForm(initial = {'UserName': my_bag.get('teacher')['username'], 'Password': my_bag.get('teacher')['password'], 'FirstName': my_bag.get('teacher')['first_name'], 'LastName': my_bag.get('teacher')['last_name'], 'Institution': my_bag.get('teacher')['institution']})


        return render(request, 'accounts/teacher_details.html', {'form':form, 'user':my_bag.get('user'), 'teacher_details':my_bag.get('teacher')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def child_delete(request):
    try:
        form = forms.ChildForm()
        import os
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
        django.setup()
        usr = Account.objects.get(username = my_bag.get('child')['username'])
        usr.delete()
        return render(request, 'accounts/institutions.html', {'form':form, 'user':my_bag.get('user'), 'institution_name':my_bag.get('institution'), 'accounts': Account.objects.values(), 'teacher_details':my_bag.get('teacher')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def games(request):
    try:    
        if request.POST:
            import os
            import django
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
            django.setup()
            game = Board.objects.get_or_create(category=my_bag.get('category')[0], data=input_json_format_converter(my_bag.get('category')[1]))[0]
            game.save()
        elif my_bag.get('user')['role'] == 'Child' and request.GET:
            import os
            import django
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
            django.setup()
            user = Account.objects.get(username = my_bag.get('user')['username'])
            user.categories = updated_score_for_category(my_bag.get('user')['categories'], my_bag.get('game')['category'], int(request.GET['score']))
            user.rating = user.rating+int(request.GET['score'])
            user.save()
            my_bag.get('user')['rating']+=int(request.GET['score'])
        if my_bag.get('user')['role'] == 'Kindergarden':
            return render(request, 'accounts/games.html', {'user':my_bag.get('user') , 'games': Board.objects.values('category'), 'categories' : listed_categories()})
        if my_bag.get('user')['role'] == 'Child':
            listed_games(my_bag.get('user')['categories'].keys())
            return render(request, 'accounts/games.html', {'user':my_bag.get('user') , 'games': listed_games(my_bag.get('user')['categories'].keys())})
        #TODO insert to an admin user enter per game amount...
        return render(request, 'accounts/games.html', {'user':my_bag.get('user') , 'games': Board.objects.values('category')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def new_game(request):
    try:
        form = forms.SingleForm()
        return render(request, 'accounts/new_game.html', {'form' : form, 'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def game_info(request):
    try:
        if request.POST:
            my_bag.set('category', [request.POST['data'], {}])
            if my_bag.get('topics'):
                left = len(my_bag.get('topics'))
            else:
                left = 8
        else:
            left = 8-len(my_bag.get('category')[1])
        form = forms.SingleForm()
        return render(request, 'accounts/game_info.html', {'massage': left, 'form': form, 'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def game_topic(request):
    try:
        if request.GET:
            my_bag.get('category')[1][request.GET['data']]=[]
            my_bag.set('topic', request.GET['data'])
            form = forms.DoubleForm()
            return render(request, 'accounts/game_topic.html', {'massage': 'first', 'form': form, 'user':my_bag.get('user')})
        else:
            my_bag.get('category')[1][my_bag.get('topic')].append(request.POST['data1'])
            my_bag.get('category')[1][my_bag.get('topic')].append(request.POST['data2'])
            form = forms.SingleForm()
            return render(request, 'accounts/game_topic.html', {'massage': 'extra', 'form': form, 'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def extra_card(request):
    try:
        if request.POST:
            my_bag.get('category')[1][my_bag.get('topic')].append(request.POST['data'])
            form = forms.SingleForm()
            return render(request, 'accounts/game_topic.html', {'massage': 'extra', 'form': form, 'user':my_bag.get('user')})
        return render(request, 'accounts/game_info.html', {'massage': left, 'form': form, 'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def done_extra(request):
    try:
        return render(request, 'accounts/game_info.html', {'massage': left, 'form': form, 'user':my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def input_json_format_converter(input_game):
    try:
        json_format = {}
        for key in input_game.keys():
            json_format[key] = {}
            i=0
            for card in input_game[key]:
                json_format[key][str(i)] = card
                i+=1
        return json_format
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def play_game(request):
    try:
        if request.GET:
            if 'add' in request.GET:
                if request.GET['game'] not in my_bag.get('user')['categories'].values():
                    import os
                    import django
                    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')
                    django.setup()
                    user = Account.objects.get(username = my_bag.get('user')['username'])
                    user.categories = jasonedCategories(my_bag.get('user')['categories'],request.GET['game'])
                    user.save()
                    for user in Account.objects.values():
                        if user['institution'] == my_bag.get('user')['institution']:
                            if user['username'] == my_bag.get('user')['username']:
                                my_bag.set('user', user)
                            else:
                                print(user)
                                usr = Account.objects.get(username=user['username'])
                                usr.categories = jasonedScore(user['categories'], request.GET['game'])
                                usr.save()
                return render(request, 'accounts/games.html', {'user':my_bag.get('user') , 'games': Board.objects.values('category'), 'categories' : listed_categories()})           

            request.GET['game']
            print("here \n\n\n")
            for game in Board.objects.values():
                if game['category'] == request.GET['game']:
                    break
            card_data = {}
            for key in game['data'].keys():
                card_data[key] = []
                for card in game['data'][key]:
                    card_data[key].append(game['data'][key][card])

            topics = sample(card_data.keys(),int(request.GET['difficulty']))

            board=[]
            for i in range(int(request.GET['difficulty'])):
                board.append(sample(card_data[topics[i]], 2))
                board[i].append(topics[i])

            return render(request, 'game/play.html',{'board': board, 'difficulty':request.GET['difficulty'], 'user': my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def difficulty(request):
    try:
        if request.GET:
            for game in Board.objects.values():
                if game['category'] == request.GET['game']:
                    break
            score = my_bag.get('user')['rating']
            categoryscore = my_bag.get('user')['categories'][request.GET['game']]
            my_bag.set('game', game)
            return render(request, 'accounts/difficulty.html',{'user': my_bag.get('user'), 'score': score, 'categoryscore':int(categoryscore), 'game':request.GET['game']})
            
        else:
            
            card_data = {}
            for key in my_bag.get('game')['data'].keys():
                card_data[key] = []
                for card in my_bag.get('game')['data'][key]:
                    card_data[key].append(my_bag.get('game')['data'][key][card])

            topics = sample(card_data.keys(),int(request.POST['difficulty']))

            board=[]
            for i in range(int(request.POST['difficulty'])):
                board.append(sample(card_data[topics[i]], 2))
                board[i].append(topics[i])

            return render(request, 'game/play.html',{'board': board, 'difficulty' : request.POST['difficulty'], 'user': my_bag.get('user')})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})


def score_board(request):
    try:
        if my_bag.get('user')['role'] == 'Kindergarden':
            return render(request, 'accounts/score_board.html', {'user': my_bag.get('user'), 'users':listed_players(Account.objects.all().filter(institution = my_bag.get('user')['institution'], role = "Child").values('first_name', 'last_name', 'rating', 'categories'))})
        else:return render(request, 'accounts/score_board.html', {'user': my_bag.get('user'), 'users':listed_players(Account.objects.all().filter(role = "Child").values('first_name', 'last_name', 'rating', 'categories'))})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})


def search(request):
    try:
        if request.GET:
            users = []
            name = request.GET['name'].split()
            if len(name) == 1:
                if my_bag.get('user')['role'] == 'Kindergarden':
                    users.append(Account.objects.filter(role='Child', first_name=name[0], institution=my_bag.get('user')['institution']).values('first_name', 'last_name', 'rating', 'categories'))
                    users.append(Account.objects.filter(role='Child', last_name=name[0], institution=my_bag.get('user')['institution']).values('first_name', 'last_name', 'rating', 'categories'))
                else:
                    users.append(Account.objects.filter(role='Child', first_name=name[0]).values('first_name', 'last_name', 'rating', 'categories'))
                    users.append(Account.objects.filter(role='Child', last_name=name[0]).values('first_name', 'last_name', 'rating', 'categories'))
            else:
                for i in range(len(name) + 1):
                    first = ""
                    last = ""
                    for j in range(len(name)):
                        if j < i:
                            if first == "":
                                first += name[j]
                            else:
                                first += " " + name[j]
                        else:
                            if last == "":
                                last += name[j]
                            else:
                                last += " " + name[j]
                    if last == "":
                        if my_bag.get('user')['role'] == 'Kindergarden':
                            users.append(Account.objects.filter(role='Child', first_name=first, institution=my_bag.get('user')['institution']).values('first_name', 'last_name', 'rating', 'categories'))
                        else:
                            users.append(Account.objects.filter(role='Child', first_name=first).values('first_name', 'last_name', 'rating', 'categories'))
                    elif first == "":
                        if my_bag.get('user')['role'] == 'Kindergarden':
                            users.append(Account.objects.filter(role='Child', last_name=last, institution=my_bag.get('user')['institution']).values('first_name', 'last_name', 'rating', 'categories'))
                        else:
                            users.append(Account.objects.filter(role='Child', last_name=last).values('first_name', 'last_name', 'rating', 'categories'))

                    else:
                        if my_bag.get('user')['role'] == 'Kindergarden':
                            users.append(Account.objects.filter(role='Child', first_name=first, last_name=last, institution=my_bag.get('user')['institution']).values('first_name', 'last_name', 'rating', 'categories'))
                        else:
                            users.append(Account.objects.filter(role='Child', first_name=first, last_name=last).values('first_name', 'last_name', 'rating', 'categories'))
                            
        
        return render(request, 'accounts/score_board.html', {'user': my_bag.get('user'), 'users': listed_players(listed_players_helper(users))})
    except:
        return render(request, 'accounts/games.html', {'user': {'role':'error'}})

def listed_categories():
    result = []
    for val in my_bag.get('user')['categories'].values():
        result.append(val)
    return result

def jasonedCategories(categories,category):
    categories[str(len(categories.keys()))] = category
    return categories

def jasonedScore(categories,category):
    categories[category] = "0"
    return categories

def listed_games(categories):
    result = []
    for category in categories:
        temp = {}
        temp['category'] = category
        result.append(temp)
    return result

def updated_score_for_category(categories, category, score):
    categories[category] = str(int(categories[category])+score)
    return categories

def listed_players(data):
    users = []
    for user in data:
        each_user = []
        each_user.append([user['first_name'] + " " + user['last_name'], user['rating']])
        for key, value in user['categories'].items():
            each_user.append([key, value])
        users.append(each_user)
    return users

def listed_players_helper(data):
    new_data = []
    for list_ in data:
        for dict_ in list_:
            new_data.append(dict_)
    return new_data

