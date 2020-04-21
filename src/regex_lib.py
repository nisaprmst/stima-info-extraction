import re
from nltk.tokenize import sent_tokenize
from kmp_lib import search_keyword_kmp
from boyer_moore_lib import search_keyword_bm


def extract_date(sentence):
    result = None
    day = re.search('senin|selasa|rabu|kamis|jum\'at|jumat|sabtu|minggu', sentence, re.IGNORECASE)
    ddmmyy = '((0?[1-9]|[12][0-9]|3[01])[-/](0?[1-9]|1[012])[-/](\d{4}|\d{2}))'
    yymmdd = '((\d{4}|\d{2})[-/](0?[1-9]|1[012])[-/]([12][0-9]|3[01]|0?[1-9]))'
    bulan = '(0?[1-9]|[12][0-9]|3[01]) (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) (\d{4}|\d{2})'
    bul = '(0?[1-9]|[12][0-9]|3[01]) (Jan|Feb|Mar|Apr|Mei|Jun|Jul|Aug|Sep|Okt|Nov|Des) (\d{4}|\d{2})'
    month = '(Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember|Jan|Feb|Mar|Apr|Mei|Jun|Jul|Aug|Sep|Okt|Nov|Des)(,( )*)*([12][0-9]|3[01]|0?[1-9])'
    date = ddmmyy + '|' + yymmdd + '|' + bulan + '|' + bul + '|' + month
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


def extract(data, keyword):
    article_date = 'tidak ditemukan tanggal'
    date = article_date
    number = 'tidak ditemukan angka'
    res = []
    for i in range(len(data)):
        sentence = data[i]
        if article_date == 'tidak ditemukan tanggal':
            d = extract_date(sentence)
            if d is not None:
                article_date = d
        match = re.search(keyword, sentence, re.IGNORECASE)
        if match is not None:
            c = 'none'
            # print(sentence)
            dt = extract_date(sentence)
            if dt is not None:
                date = dt
            before = '(?i)' + keyword + '(?:\D{0,100})[^.,] (\d{1,3}(\.\d{3}])*)'
            after = '(?i)(\d{1,3}(\.\d{3}])*)[^.,] (?:\D{0,100})' + keyword
            b = re.search(before, sentence, re.IGNORECASE)
            a = re.search(after, sentence, re.IGNORECASE)
            bef = keyword
            af = keyword
            if b is not None:
                bef = b.group()
            if a is not None:
                af = a.group()
            if bef != keyword:
                c = bef
                if af != keyword and len(af) < len(bef):
                    c = af
            else:
                if af != keyword:
                    c = af
            if c != 'none':
                cregex = re.search('(\d{1,3}(\.\d{3}])*)', c)
                number = cregex.group()
            res.append([date, number])
    if date == 'tidak ditemukan tanggal':
        date = article_date
    return res

        

            

print(extract_date('hari ini Jumat (2000/12/31)'))
print(extract_date('hari ini Jum\'at (31/12/1212)'))
print(extract_date('hari ini Jum\'at 3 September 2020'))
print(extract_date('hari ini Jum\'at des, 15 jam 12:23 WIb'))

filename = 'test.txt'
file = open(filename, "r")
text = file.read()
print(text)

data = sent_tokenize(text)

keyword = str(input("Masukkan keyword: "))
res = search_keyword_bm(data, keyword)
ex = extract(res, keyword)

for i in range(len(ex)):
    print('Jumlah:', ex[i][1])
    print('Waktu: ', ex[i][0])
    # print(res[i])