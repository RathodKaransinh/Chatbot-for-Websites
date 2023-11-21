from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from nltk.tokenize import word_tokenize

def find_list():
    f = open("E:/Django projects/all.txt",'r')
    lines = f.readlines()
    urls_list = []
    urls_keyword = []
    i=1
    for line in lines:
        # print(line,i)
        i += 1
        line = line.replace('\n','')
        line = line.split(',')
        urls_list.append(line[0])
        urls_keyword.append(line[1])
    f.close()
    
    return urls_list, urls_keyword

def find_link(query):
    tokens = query.split(' ')
    urls_list , urls_keyword = find_list()
    j = 0
    count = []
    
    for i in urls_keyword:
        count.append(0)
        for word in tokens:
            if word in i:
                count[j] = count[j] + 1
        j = j+1
    
    j, ans = 0, 0
    max = 0
    for cnt in count:
        if(max<cnt):
            max = cnt
            ans = j
        j = j+1

    if (max==0):
        return "Nothing found"
    else:
        return urls_list[ans]

def index(request):
    return render(request, "chat1/index3.html")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    # print(userMessage+'getresponse')
    reply = find_link(userMessage.lower())
    # userMessage2 = find_link1(userMessage.lower())
    return HttpResponse(reply)


