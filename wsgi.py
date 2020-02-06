from flask import Flask, render_template,request
import MySQLdb

application = Flask(__name__, template_folder='templates')

@application.route('/')
def index():
  return render_template('welcome.html')

# @application.route('/data', methods=['GET', 'POST'])
# def data():
            # conn = MySQLdb.connect(host='mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            # cursor = conn.cursor()
            # if request.method == "POST":
             # details = request.form
             # fromdisc = details['fromdisc']
             # todisc = details['todisc']
             # query = "SELECT PP.list_price,PS.description,PP.discount,PS.catalogue_category from XXIBM_PRODUCT_PRICING PP INNER JOIN XXIBM_PRODUCT_SKU PS ON PP.item_number=PS.item_number where  PP.discount BETWEEN %s AND %s"
             # cursor.execute(query, (fromdisc, todisc))
             # data = cursor.fetchall()
             # print("Total number of rows: ", cursor.rowcount)
             # print("\nPrinting record")
             # for row in data:
               # print("list_price = ", row[0])
               # print("description = ", row[1])
               # print("discount = ", row[2])
               # print("catalogue_category = ", row[3])
             # return render_template('product.html', data=data)

@application.route('/apparels', methods=["GET", "POST"])
def apparels():
            conn = MySQLdb.connect(host='custom-mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            if request.method == "GET":
              details = request.form
              query = "select distinct class_name from sampledb.XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME='Clothing' order by class_name"
              cursor.execute(query)
              clsData = cursor.fetchall()              
              return render_template('apparels.html', apparels=clsData)

@application.route('/footwears', methods=["GET", "POST"])
def footwears():
            conn = MySQLdb.connect(host='custom-mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            if request.method == "GET":
              details = request.form
              query = "select distinct class_name from sampledb.XXIBM_PRODUCT_CATALOGUE WHERE FAMILY_NAME='Footwear' order by class_name"
              cursor.execute(query)
              clsData = cursor.fetchall()
              print("Total number of rows: ", cursor.rowcount)
              print("\nPrinting record")
              for row in clsData:
                print("Available Class = ", row[0])
              return render_template('footwears.html', footwears=clsData)  
              
@application.route('/athwear', methods=["GET", "POST"])
def athwear():
            conn = MySQLdb.connect(host='custom-mysql.gamification.svc.cluster.local',user='xxuser',passwd='welcome1',db='sampledb')
            cursor = conn.cursor()
            if request.method == "GET":
              details = request.form
              query = "SELECT distinct PS.DESCRIPTION,PST.BRAND,PS.SKU_ATTRIBUTE_VALUE1,PS.SKU_ATTRIBUTE_VALUE2 FROM sampledb.XXIBM_PRODUCT_CATALOGUE PC , sampledb.XXIBM_PRODUCT_SKU PS , sampledb.XXIBM_PRODUCT_STYLE PST , sampledb.XXIBM_PRODUCT_PRICING PP WHERE PC.COMMODITY= PS.CATALOGUE_CATEGORY and PC.COMMODITY= PST.CATALOGUE_CATEGORY AND PS.ITEM_NUMBER=PP.ITEM_NUMBER AND PC.CLASS_NAME='Athletic wear' and PP.IN_STOCK='Yes'"
              cursor.execute(query)
              desData = cursor.fetchall()   
              print("Total number of rows: ", cursor.rowcount)
              print("\nPrinting record")
              for row in desData:
                print("Available Class = ", row[0])              
            return render_template('selection.html', athwear=desData)   

if __name__ == '__main__':
    application.run()