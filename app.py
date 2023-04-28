from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
from database import user
app = Flask(__name__)
@app.route('/')
def notdash():
   df = user()
   fig = px.bar(df, x='IdCapteur', y=['humidity','temperature'], barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
