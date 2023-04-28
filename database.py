from sqlalchemy import create_engine, text
import pandas as pd

db_Connection_string = 'mysql+pymysql://gqkafym644stvaz63r28:pscale_pw_R3G4SXVb80TpwJssH9iblTuoZETtaD9HUlJdlhD5629@aws.connect.psdb.cloud/testdatabase'

engine = create_engine(db_Connection_string,
    connect_args={
        "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def user():
    with engine.connect() as conn:
        result = conn.execute(text("select * From capteur ORDER BY IdCapteur DESC"))

        resultDict = []

        for row in result.all():
            resultDict.append(row._asdict())

        df = pd.DataFrame(resultDict)
        return df