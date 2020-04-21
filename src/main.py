from flask import Flask
from flask import render_template
from flask import request, redirect
from werkzeug.utils import secure_filename
from lib.boyer_moore_lib import search_keyword_bm
from lib.regex_lib import search_keyword_regex, extract, search_article_date
from lib.kmp_lib import search_keyword_kmp
from nltk.tokenize import sent_tokenize
import os

# from werkzeug import secure_filename
app = Flask(__name__, template_folder='view')
# Create a directory in a known location to save files to.
uploads_dir = os.path.join(os.path.dirname(app.instance_path), 'text')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/beranda')
def beranda():
   return render_template('index.html')

@app.route('/perihal')
def perihal():
   return render_template('perihal.html')

@app.route('/ekstrak', methods=["GET", "POST"])
def ekstrak():
   return render_template('ekstrak.html')

@app.route('/hasil', methods=["GET", "POST"])
def hasil():
   if request.method == "POST":
      keyword = request.form['keyword']
      data = request.files['file']
      algo = request.form['algo']
      # data.save(secure_filename(data.filename))
      data.save(os.path.join(uploads_dir, "test.txt"))
      filename = 'text/test.txt'
      file = open(filename, "r")
      text = file.read()
      print(text)

      data = sent_tokenize(text)
      article_date = search_article_date(data)
      if algo == '1':
         res = search_keyword_kmp(data, keyword)
      elif algo == '2':
         res = search_keyword_bm(data, keyword)
      else:
         res = search_keyword_regex(data, keyword)

      extraction = extract(res, keyword, article_date)
      print(extraction)
      error = 'Keyword tidak ditemukan'
      if len(extraction) != 0:
         error = ''
         for i in range(len(extraction)):
             print('Jumlah:', extraction[i][1])
             print('Waktu: ', extraction[i][0])
      return render_template('hasil.html', keyword = keyword, error = error, extraction = extraction, res = res, len = len(extraction))


if __name__ == '__main__':
   app.run(port=8080, debug=True)