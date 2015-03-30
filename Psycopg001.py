import psycopg2

# Connect to an existing database
conn = psycopg2.connect('dbname=lisa user=lisa')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute(
	'''
		CREATE TABLE if NOT EXISTS employee (
			firstname varchar(40),
			lastname varchar(40),
			age numeric(3),
			city varchar(20)
		);
	'''
)

# Prompt user for information
first = raw_input("what is your first name? ")
last = raw_input("what is your last name? ")
age = raw_input("how old are you? ")
city = raw_input("what city do you live in? ")


# Pass data to fill table
cur.execute(
	'''
		INSERT INTO employee
			(firstname, lastname, age, city)
		VALUES 
			(%s, %s, %s, %s);
	''',
	(first, last, age, city)
)

# Query the database ad obtain data as Python objects
cur.execute('SELECT * FROM employee;')
row_fetch = cur.fetchall()
print row_fetch

# make the changes to the database persistent
conn.commit()

cur.close()
conn.close()