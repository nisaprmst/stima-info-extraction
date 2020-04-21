import re
from nltk.tokenize import sent_tokenize


def search_date(sentence):
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

def extract(data, keyword):
    article_date = 'tidak ditemukan tanggal'
    date = article_date
    number = 'tidak ditemukan angka'
    res = []
    for i in range (len(data)):
        sentence = data[i]
        if article_date == 'tidak ditemukan tanggal':
            d = search_date(sentence)
            if d is not None:
                article_date = d
        match = re.search(keyword, sentence, re.IGNORECASE)
        if match is not None:
            # print(sentence)
            dt = search_date(sentence)
            if dt is not None:
                date = dt
            before = '(?i)' + keyword + '(?:\D{0,100})[^.,] ([0-9][0-9,]*)'
            after = '(?i)([0-9][0-9,]*)[^.,] (?:\D{0,100})' + keyword
            b = re.search(before, sentence, re.IGNORECASE)
            a = re.search(after, sentence, re.IGNORECASE)
            bef = keyword
            af = keyword
            if b is not None:
                bef = b.group()
            if a is not None:
                af = a.group()
            if bef != keyword:
                number = bef
                if af != keyword and len(af) < len(bef):
                    number = af
            else:
                if af != keyword:
                    number = af
            res.append([date, number])
    if date == 'tidak ditemukan tanggal':
        date = article_date
    return res

        

            

print(search_date('hari ini Jumat (2000/12/31)'))
print(search_date('hari ini Jum\'at (31/12/1212)'))
print(search_date('hari ini Jum\'at 3 September 2020'))
print(search_date('hari ini Jum\'at des, 15 jam 12:23 WIb'))

filename = 'test.txt'
file = open(filename, "r")
text = file.read()
print(text)

data = sent_tokenize(text)

keyword = str(input("Masukkan keyword: "))
ex = extract(data, keyword)

for i in range(len(ex)):
    print('Jumlah:', ex[i][1])
    print('Waktu: ', ex[i][0])