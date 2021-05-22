import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
import urllib.parse

def create_app():
    app = Flask(__name__)
    client = MongoClient('mongodb+srv://aravind:'+urllib.parse.quote('@Ravind1')+'@cluster0.zgjkp.mongodb.net/microblog?retryWrites=true&w=majority')
    app.db = client.microblog


    @app.route('/',methods=['GET','POST'])
    def Hello():
        # print([e for e in app.db.entries.find({})])
        entries1=[]
        if request.method == 'POST':
            entry_content = request.form.get('content')
            date = datetime.datetime.today().strftime('%d-%m-%y')
            formatted_date=datetime.datetime.strptime(date,'%d-%m-%y').strftime('%b %d')
            # entries.append((entry_content, formatted_date))
            app.db.entries.insert({'content':entry_content, 'date':formatted_date})
        entries1 = [
            (
                entry['content'],
                entry['date']  
            )
            for entry in app.db.entries.find({})
        ]
        return render_template('home.html', entries=entries1)
    
    return app