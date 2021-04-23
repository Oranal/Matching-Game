from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from game.models import *
from accounts.viewbag import view_bag
import random

my_bag = view_bag()

def play(request):
    random_filler()
    return render(request, 'game/play.html', random_filler_holidays())

def random_filler():
    fakedb = {1: ['2-1', '3-2', '7-6'],
                2: ['4-2', '1+1', '6-4'], 
                3: ['2+1', '6-3', '7-4'], 
                4: ['2+2', '8-4', '9-5'], 
                5: ['2+3', '1+4', '8-3'], 
                6: ['2+4', '3+3', '1+5'], 
                7: ['4+3', '5+2', '9-2'], 
                8: ['3+5', '4+4', '2+6'],
                9: ['5+4', '6+3', '1+8'],
                10: ['5+5', '7+3', '1+9']}
    x = {}
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sample = random.sample(numbers, 4)

    first = random.sample(fakedb[sample[0]], 2)
    first.append(sample[0])
    second = random.sample(fakedb[sample[1]], 2)
    second.append(sample[1])
    third = random.sample(fakedb[sample[2]], 2)
    third.append(sample[2])
    fourth = random.sample(fakedb[sample[3]], 2)
    fourth.append(sample[3])

    # print(first)
    x['one'] = first
    x['two'] = second
    x['three'] = third
    x['four'] = fourth
    return x

def random_filler_holidays():
    fakedb = {'חנוכה': ['סביבון', 'סופגניה', 'חנוכיה'],
                'ראש-השנה': ['שופר', 'רימון', 'תפוח בדבש'], 
                'פסח': ['יציאת מצרים', 'פרעה', 'מצות'], 
                'פורים': ['תחפושת', 'אוזן המן', 'רעשן'], 
                'סוכות': ['אתרוג', 'סוכה', 'ארבעת המינים'], 
                'ט"ו-בשבט': ['פירות יבשים', 'נטיעה', 'אילן'], 
                'ל"ג-בעומר': ['תפוחי אדמה', 'אש', 'מדורות']
                }
    x = {}
    holidays = ['חנוכה', 'ל"ג-בעומר', 'ט"ו-בשבט', 'סוכות', 'פורים', 'פסח', 'ראש-השנה']
    sample = random.sample(fakedb.keys(), 4)

    first = random.sample(fakedb[sample[0]], 2)
    first.append(sample[0])
    second = random.sample(fakedb[sample[1]], 2)
    second.append(sample[1])
    third = random.sample(fakedb[sample[2]], 2)
    third.append(sample[2])
    fourth = random.sample(fakedb[sample[3]], 2)
    fourth.append(sample[3])

    # print(first)
    x['one'] = first
    x['two'] = second
    x['three'] = third
    x['four'] = fourth
    return x