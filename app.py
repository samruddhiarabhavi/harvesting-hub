from flask import Flask, render_template, url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='plant1'

mysql=MySQL(app)

@app.route("/")
def index():
    return "<h1>Hello Python</h1>"

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        details=request.form
        username=details['usernm']
        password=details['pass']
        cur=mysql.connection.cursor()

        return render_template('login.html')

@app.route("/register",methods=['POST','GET'])
def register():
    if request.method == "POST":
        details = request.form
        reg_name = details['name']
        reg_address = details['address']
        reg_phone = details['phone']
        reg_email = details['email']
        reg_password = details['password']
        cur=mysql.connection.cursor()
        cur.execute("insert into tbl_register(name,password,Email,contact_no,address) values (%s,%s,%s,%s,%s)", (reg_name,reg_password,reg_email,reg_phone,reg_address,))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('register.html')


@app.route("/season")
def season():

    return render_template('season.html')

@app.route("/add_category",methods=['POST','GET'])
def add_category():
    if request.method == "POST":
        details = request.form
        cat_name = details['cname']
        cat_scname = details['scname']
        cat_image = details['cimage']
        cat_des = details['cdes']
        cur=mysql.connection.cursor()
        cur.execute("insert into tbl_cetegory(Category_name,sub_cat_nm,image,Description) values (%s,%s,%s,%s)", (cat_name, cat_scname, cat_image,cat_des))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('add_category.html')



@app.route("/add_plant",methods=['POST','GET'])
def add_plant():
    if request.method == "POST":
        details = request.form
        plant_name = details['plantname']
        plant_image = details['plantimage']
        plant_des = details['description']
        plant_price = details['price']
        plant_discount = details['discount']
        plant_cat = details['catname']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_plant(plant_name,image,description,price,discount,Category_name) values (%s,%s,%s,%s,%s)",( plant_name,plant_image,plant_des,plant_price,plant_discount,plant_cat ))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('add_plant.html')



@app.route("/order_list",methods=['POST','GET'])
def order_list():
    if request.method == "POST":
        details = request.form
        list_name = details['plantname']
        list_image = details['image']
        list_des = details['description']
        list_price = details['price']
        list_discount = details['discount']
        list_cat = details['catname']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_order(plant_name,image,description,price,discount,category_name) values (%s,%s,%s,%s,%s)", (list_name,list_image,list_des,list_price,list_discount,list_cat))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('order_list.html')


@app.route("/feedback",methods=['POST','GET'])
def feedback():
    if request.method == "POST":
        details = request.form
        feed_name = details['username']
        feed_address = details['address']
        feed_content = details['content']
        feed_comment = details['comment']
        feed_text = details ['text']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_feedback(user name,address,contact_no,commant,text) values (%s,%s,%s,%s,%s)", (feed_name,feed_address,feed_content,feed_comment,feed_text))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('feedback.html')

@app.route("/addbc",methods=['POST','GET'])
def addbc():
    if request.method == "POST":
        details = request.form
        addbc_name = details['plantname']
        addbc_description = details['description']
        addbc_price= details['price']
        addbc_discount = details['discount']
        addbc_categoryName= details['categoryName']
        addbc_location = details['location']

    return render_template('addbc.html')

@app.route("/ulogin")

def ulogin():
    if request.method=='POST':
        details=request.form
        username=details['usernm']
        upassword=details['upass']
        cur=mysql.connection.cursor()

        return render_template('login.html')



@app.route("/uredister")
def uredister():
    if request.method=='POST':
        details=request.form
        ured_name=details['name']
        ured_add=details['address']
        ured_con=details['contact_no']
        ured_email=details['Email']
        ured_pass=details['password']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_uregister(name,address,contact_no,Email,password) values (%s,%s,%s,%s,%s)",(ured_name,ured_add,ured_con,ured_email, ured_pass))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('uredister.html')


@app.route("/booking",methods=['POST','GET'])
def booking():
    if request.method == "POST":
        details = request.form
        book_name = details['plantname']
        book_address = details['address']
        book_content = details['content']
        book_date = details['date']
        book_totalAmount = details['totalAmount']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_booking(user_name,address,contect_no,date,total_amount	) values (%s,%s,%s,%s,%s)",(book_name,book_address,book_content,book_date,book_totalAmount))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('booking.html')


@app.route("/pyment",methods=['POST','GET'])
def pyment():
    if request.method == "POST":
        details = request.form
        pay_payment = details['payment-method']
        pay_upi = details['"upi-details']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_pyment(upi,credit/debit) values (%s,%s,%s)", (pay_payment,pay_upi))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('payment.html')


@app.route("/card",methods=['POST','GET'])
def card():
    if request.method == "POST":
        details = request.form
        card_name= details['name']
        card_no = details['cardNumber']
        card_cvc = details['cvc']
        card_billAddress = details['billAddress']
        card_amont = details['amount']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_pyment(name,card_no,Expition_data,cvc_data,bill_address,amount) values (%s,%s,%s,%s,%s,%s)",(card_name,card_no,card_cvc,card_billAddress,card_amont))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('card.html')


@app.route("/upi",methods=['POST','GET'])
def upi():
    if request.method == "POST":
        details = request.form
        upi_name = details['name']
        upi_id = details['upiId']
        upi_amount = details['amount']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_pyment(name,upiid,amount) values (%s,%s,%s)",(upi_name,upi_id,upi_amount))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
    return render_template('upi.html')

@app.route("/uorder",methods=['POST','GET'])
def uorder():
    if request.method == "POST":
      details=request.form
      list_name = details['plantName']
      list_image = details['image']
      list_description = details['description']
      list_price = details['price']
      list_discount = details['discount']
      list_categoryName = details['categoryName']
      list_location = details['location']
      cur = mysql.connection.cursor()
      cur.execute("insert into tbl_order(plant_name,image,description,price,discount,Category_name,location) values (%s,%s,%s,%s,%s,%s,%s)",(list_name,list_image,list_description,list_price,list_discount,list_categoryName,list_location))
      mysql.connection.commit()
      cur.close()
      return "Record Inserted"
    return render_template('my_order.html')


@app.route("/ufeedback",methods=['POST','GET'])
def ufeedback():
    if request.method == "POST":
        details = request.form
        ufeed_name = details['username']
        ufeed_address = details['address']
        ufeed_content = details['content']
        ufeed_comment = details['comment']
        ufeed_text = details['text']
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_pyment(user_name,address,contect_no,commant,text) values (%s,%s,%s,%s,%s)",(ufeed_name,ufeed_address,ufeed_content ,ufeed_comment,ufeed_text))
        mysql.connection.commit()
        cur.close()
        return "Record Inserted"
        return render_template('ufeedback.html')


if __name__ =="__main__":
    app.debug=True
    app.run()