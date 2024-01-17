from flask import Flask, render_template, request, send_file
import pandas as pd
from geopy.geocoders import Nominatim
from flask_table import Table, Col, create_table
import io

def create_table_class(lst):
    TableCls = create_table('MyTable')
    for i in lst:
        TableCls = TableCls.add_column(i, Col(i))
    return TableCls

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods = ['GET'])
def invalid():
    return "Calling this is not valid, go to / instead!"

def get_table(df):
    columns = df.columns.values
    # rows = df.T.to_dict().values()
    header = [df.index.name]
    header.extend(columns)

    rows = []
    for index, row in df.iterrows():
        tr = row.to_dict()
        tr[df.index.name] = index
        rows.append(tr)

    #print(header)
    #print(rows)
    table_class = create_table_class(header)
    table = table_class(rows)
    #print(table.__html__())
    return table

@app.route('/submit', methods = ['POST'])
def submit():
    file = request.files['choose']
    df = pd.DataFrame.from_csv(file)

    for index, row in df.iterrows():
        nom = Nominatim(timeout = 200)
        try:
            location = nom.geocode(row['address'])
        except:
            location = nom.geocode(row['Address'])
        df.at[index, 'Latitude'] = location.latitude
        df.at[index, 'Longitude'] = location.longitude
    
    file = pd.DataFrame.to_csv(df)
    #print(file)
    table = get_table(df)

    return render_template("download.html", table = table, file = file)

@app.route('/download', methods = ['POST'])
def download():
    table = request.form.get('table')
    return send_file(io.BytesIO(table.encode('utf-8')), mimetype = "text/csv")

# @app.before_request
def before_request():
    #print(request.values, request.get_json(), request.get_data())
    print(request.content_length)
    print(request.content_type)
    print(request.content_encoding)
    print(request.args)
    print(request.form)
    table = request.form.get('table')
    print(table)
    for k, v in request.form.items():
        print(k)
        print(len(v))
        print(type(v))

if __name__ == "__main__":
    app.run(debug = True)