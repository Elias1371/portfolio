from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def keep_in_database(data):
    with open('webserver/database.txt', mode='a') as database:
        email = data['email1']
        subject = data['subject1']
        message = data['message1']
        file = database.write(f'\n{email},{subject},{message}')


def keep_in_csv(data):
    with open('webserver/database.csv', newline='', mode='a') as database2:
        email = data['email1']
        subject = data['subject1']
        message = data['message1']
        CsvFile = csv.writer(database2, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        CsvFile.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        keep_in_csv(data)
        return redirect('/tnx.html')
    else:
        print('sth is wrong')
# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/components.html")
# def comp():  # component nazadam emtehani
#     return render_template('components.html')


# @app.route("/contact.html")
# def cont():  # contact nazadam emtehani
#     return render_template('contact.html')


# @app.route("/blog")
# def blog():
#     return "<p>خداوکیلی آسون نیست ولی مشکلی نیست که آسان نشود</p>"


# @app.route("/blog/2020")
# def blog2():
#     return "<p>toye ayne bebin che zoode zood</p>"
