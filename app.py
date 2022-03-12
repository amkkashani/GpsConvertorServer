import decimal
import sys

from flask import Flask
import pymap3d as pm
from flask import request

app = Flask(__name__)


@app.route('/convert')
def convertor():
    # lat0 = 35.688722218333  # deg
    # lon0 = 51.438900521667  # deg
    # h0 = 1189.362061  # meters
    #
    # # The point of interest ("x":"51.439001528333","y":"35.688969975000","z":"1188.442993")
    # lat = 35.688734683333  # deg
    # lon = 51.438907011667  # deg
    # h = 1189.375977  # meters
    lat = float(request.args.get("lat"))
    lon = float( request.args.get("lon"))
    h = float( request.args.get("h"))

    lat0 = float(request.args.get("lat0"))
    lon0 = float(request.args.get("lon0"))
    h0 = float(request.args.get("h0"))

    print("" + lat.__str__() + " " + lon.__str__() + " " + h.__str__())
    print("" + lat.__str__() + " " + lon.__str__() + " " + h.__str__(), file=sys.stdout)
    result = pm.geodetic2enu(lat, lon, h, lat0, lon0, h0)
    # print(result)
    return result.__str__()


if __name__ == '__main__':
    app.run()
