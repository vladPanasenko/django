from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    ft = request.GET['text-here']
    fts = len(ft)
    ftw = ft.split()

    w_dict = {}

    for w in ftw:
        if w in w_dict:
            w_dict[w] += 1
        else:
            w_dict[w] = 1

    s_dict = sorted(w_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': ft, 'sym': fts,
                  'words': len(ftw), 'dict': s_dict})

