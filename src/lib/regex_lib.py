import re
from .kmp_lib import search_keyword_kmp
from .boyer_moore_lib import search_keyword_bm


def extract_date(sentence):
    result = None
    day = re.search('senin|selasa|rabu|kamis|jum\'at|jumat|sabtu|minggu', sentence, re.IGNORECASE)
    a = '((0?[1-9]|[12][0-9]|3[01])[-/](0?[1-9]|1[012])[-/](\d{4}|\d{2}))'
    b = '((\d{4}|\d{2})[-/](0?[1-9]|1[012])[-/]([12][0-9]|3[01]|0?[1-9]))'
    c = '(0?[1-9]|[12][0-9]|3[01])* (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) (\d{4}|\d{2})*'
    d = '(0?[1-9]|[12][0-9]|3[01])* (Jan|Feb|Mar|Apr|Mei|Jun|Jul|Aug|Sep|Okt|Nov|Des) (\d{4}|\d{2})*'
    e = '(Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember|Jan|Feb|Mar|Apr|Mei|Jun|Jul|Aug|Sep|Okt|Nov|Des)(,( )*)*([12][0-9]|3[01]|0?[1-9])'
    f = '(0?[1-9]|[12][0-9]|3[01]) (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember|Jan|Feb|Mar|Apr|Mei|Jun|Jul|Aug|Sep|Okt|Nov|Des)'
    g = '((0?[1-9]|1[012])[-/]([12][0-9]|3[01]|0?[1-9]))'
    h = '((0?[1-9]|[12][0-9]|3[01])[-/](0?[1-9]|1[012]))'
    date = a + '|' + b + '|' + c + '|' + d + '|' + e + '|' + f + '|' + g + '|' + h
    date = re.search(date, sentence, re.IGNORECASE)
    waktu = re.search('(\d{2}:\d{2})|(\d{2}.\d{2}) (WIB|WITA|WIT)?', sentence, re.IGNORECASE)
    if day is not None:
        result = day.group()
        if date is not None:
            result = result + ' (' + date.group() + ')'
            if waktu is not None:
                result = result + ' pukul ' + waktu.group()
        else:
            if waktu is not None:
                result = result + ' pukul ' + waktu.group()
    else:
        if date is not None:
            result = date.group()
            if waktu is not None:
                result = result + ' pukul ' + waktu.group()
        else:
            if waktu is not None:
                result = result + ' pukul ' + waktu.group()
        
    return result

def search_keyword_regex(data, keyword):
    sentence = []
    for i in range (len(data)):
        match = re.search(keyword, data[i], re.IGNORECASE)
        if match is not None:
            sentence.append(data[i])
    return sentence

def search_article_date(data):
    article_date = 'tidak ditemukan tanggal'
    for i in range (len(data)):
        d = extract_date(data[i])
        if d is not None:
            article_date = d
            break
    return article_date


def extract(data, keyword, article_date):
    date = article_date
    res = []
    for i in range(len(data)):
        number = 'tidak ditemukan angka'
        sentence = data[i]
        match = re.search(keyword, sentence, re.IGNORECASE)
        if match is not None:
            c = 'none'
            # print(sentence)
            dt = extract_date(sentence)
            if dt is not None:
                date = dt
            before = '(?i)' + keyword + '(?:\D{0,100})[^.,](\d{1,3}(.\d{3})*(,\d)?)'
            after = '(?i)(\d{1,3}(\.\d{3})*(,\d)?)[^.,] (?:\D{0,100})' + keyword
            b = re.search(before, sentence, re.IGNORECASE)
            a = re.search(after, sentence, re.IGNORECASE)
            bef = keyword
            af = keyword
            if b is not None:
                bef = b.group()
                print(bef)
            if a is not None:
                af = a.group()
                print(af)
            print(bef, af)
            if bef != keyword:
                c = bef
                if af != keyword and len(af) < len(bef):
                    c = af
            else:
                if af != keyword:
                    c = af
            if c != 'none':
                cregex = re.search('(\d{1,3}(\.\d{3})*(,\d)?)', c)
                print(c)
                number = cregex.group()
            res.append([date, number])
    if date == 'tidak ditemukan tanggal':
        date = article_date
    return res

# print(extract_date(" 22 April lalal"))

            