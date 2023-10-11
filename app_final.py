from flask import Flask, render_template, request, redirect, url_for
#import os
#import urllib.parse as up
import psycopg2 

app = Flask(__name__) 

#up.uses_netloc.append("postgres")
#url = up.urlparse(os.environ["postgres://eovnqexx:ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB@peanut.db.elephantsql.com/eovnqexx"])

# Connect to the database 
conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

# create a cursor 
cur = conn.cursor() 

# if you already have any table or not id doesnt matter this

# will create student table for you. 
cur.execute('''CREATE TABLE IF NOT EXISTS student (student_id SERIAL PRIMARY KEY, name varchar(255), credits_earned int);''') 

# Insert some data into the table 
#cur.execute( 
#	'''INSERT INTO products (name, price) VALUES 
#	('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')

# will create instructor table for you.
cur.execute('''CREATE TABLE IF NOT EXISTS instructor (instructor_id SERIAL PRIMARY KEY, name varchar(255), course_department varchar(255));''')

# will create course table for you.
cur.execute('''CREATE TABLE IF NOT EXISTS course (course_id SERIAL PRIMARY KEY, title varchar(255), credits_worth int, instructor varchar(255), enrollment varchar(255)[][]);''')

# commit the changes 
conn.commit() 

# close the cursor and connection 
cur.close() 
conn.close() 


@app.route('/') 
def index(): 
	# Connect to the database
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432')
	#conn = psycopg2.connect(database="flask_db", 
							#user="postgres", 
							#password="root", 
							#host="localhost", port="5432") 

	# create a cursor 
	cur = conn.cursor() 

	# Select all products from the student table 
	cur.execute('''SELECT * FROM student''')

	# Fetch the data 
	data = cur.fetchall()
	
	# Select all products from the instructor table
	cur.execute('''SELECT * FROM instructor''')
	
	# Fetch the data
	data2 = cur.fetchall()
	
	# Select all products from the course table
	cur.execute('''SELECT * FROM course''')
	
	# Fetch the data
	data3 = cur.fetchall()

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return render_template('index.html', data=data, data2=data2, data3=data3) 


@app.route('/create_student', methods=['POST']) 
def create_s(): 
	#conn = psycopg2.connect(database="flask_db", 
							#user="postgres", 
							#password="root", 
							#host="localhost", port="5432")
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 
    
	# Get the data from the form 
	name = request.form['name']
	credits_earned = request.form['credits_earned']
    
	# Insert the data into the table 
	cur.execute( 
		'''INSERT INTO student 
		(name, credits_earned) VALUES (%s, %s)''', 
		(name, credits_earned)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/create_instructor', methods=['POST']) 
def create_i(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432')
	
	cur = conn.cursor() 
    
	# Get the data from the form 
	name = request.form['name']
	course_department = request.form['course_department']
    
	# Insert the data into the table 
	cur.execute( 
		'''INSERT INTO instructor 
		(name, course_department) VALUES (%s, %s)''', 
		(name, course_department)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/create_course', methods=['POST']) 
def create_c(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 
    
	# Get the data from the form 
	title = request.form['title']
	credits_worth = request.form['credits_worth']
	instructor = request.form['instructor']
    
	# Insert the data into the table 
	cur.execute( 
		'''INSERT INTO course 
		(title, credits_worth, instructor) VALUES (%s, %s, %s)''', 
		(title, credits_worth, instructor)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/update_student', methods=['POST']) 
def update_s(): 
	#conn = psycopg2.connect(database="flask_db", 
#							user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 

	# Get the data from the form 
	name = request.form['name'] 
	credits_earned = request.form['credits_earned'] 
	student_id = request.form['student_id'] 

	# Update the data in the table 
	cur.execute( 
		'''UPDATE student SET name=%s,
		credits_earned=%s WHERE student_id=%s''', (name, credits_earned, student_id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index')) 


@app.route('/update_instructor', methods=['POST']) 
def update_i(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 

	# Get the data from the form 
	name = request.form['name'] 
	course_department = request.form['course_department'] 
	instructor_id = request.form['instructor_id'] 

	# Update the data in the table 
	cur.execute( 
		'''UPDATE instructor SET name=%s,
		course_department=%s WHERE instructor_id=%s''', (name, course_department, instructor_id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index')) 


@app.route('/update_course', methods=['POST']) 
def update_c(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 

	# Get the data from the form 
	title = request.form['title'] 
	credits_worth = request.form['credits_worth']
	instructor = request.form['instructor']
	course_id = request.form['course_id']

	# Update the data in the table 
	cur.execute('''UPDATE course SET title=%s,
		credits_worth=%s, instructor=%s WHERE course_id=%s''', (title, credits_worth, instructor, course_id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index'))


@app.route('/add_student', methods=['POST']) 
def update_as(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 

	# Get the data from the form 
	student_name = request.form['student_name']
	course_id = request.form['course_id']

	# Update the data in the table 
	cur.execute('''UPDATE course SET enrolled=ARRAY_APPEND(enrolled, %s) WHERE course_id=%s''', (student_name, course_id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index'))


@app.route('/drop_student', methods=['POST']) 
def update_ds(): 
	#conn = psycopg2.connect(database="flask_db", 
	#						user="postgres", 
	#						password="root", 
	#						host="localhost", port="5432")
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432') 

	cur = conn.cursor() 

	# Get the data from the form 
	student_name = request.form['student_name']
	course_id = request.form['course_id']

	# Update the data in the table 
	cur.execute('''UPDATE course SET enrolled=ARRAY_REMOVE(enrolled, %s) WHERE course_id=%s''', (student_name, course_id)) 

	# commit the changes 
	conn.commit() 
	return redirect(url_for('index'))


@app.route('/delete_student', methods=['POST']) 
def delete_s(): 
	#conn = psycopg2.connect(database="flask_db", user="postgres", 
	#password="root", 
	#host="localhost", port="5432") 
	
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432')
	
	cur = conn.cursor()

	# Get the data from the form 
	student_id = request.form['student_id'] 

	# Delete the data from the table 
	cur.execute('''DELETE FROM student WHERE student_id=%s''', (student_id,)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index'))


@app.route('/delete_instructor', methods=['POST']) 
def delete_i(): 
	#conn = psycopg2.connect(database="flask_db", user="postgres", 
	#password="root", 
	#host="localhost", port="5432")
    
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432')
    
	cur = conn.cursor() 

	# Get the data from the form 
	instructor_id = request.form['instructor_id'] 

	# Delete the data from the table 
	cur.execute('''DELETE FROM instructor WHERE instructor_id=%s''', (instructor_id,)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index')) 


@app.route('/delete_course', methods=['POST']) 
def delete_c(): 
	#conn = psycopg2.connect(database="flask_db", user="postgres", 
	#password="root", 
	#host="localhost", port="5432")
    
	conn = psycopg2.connect(database='eovnqexx', user='eovnqexx', 
						password='ZGnmvRJb1Yr-GiMTCqm9EOiPQt5VlsyB', host='peanut.db.elephantsql.com', port='5432')
	
	cur = conn.cursor() 

	# Get the data from the form 
	course_id = request.form['course_id'] 

	# Delete the data from the table 
	cur.execute('''DELETE FROM course WHERE course_id=%s''', (course_id,)) 

	# commit the changes 
	conn.commit() 

	# close the cursor and connection 
	cur.close() 
	conn.close() 

	return redirect(url_for('index'))


if __name__ == '__main__': 
	app.run(debug=True) 

