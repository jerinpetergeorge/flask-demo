# contact-management
Simple Contact Management app

## Prerequisites
1. Python 3.x
2. Git (to clone the repo)
3. MYSQL Database

### Create and Activate virtualenv
1. `pip3 install virtualenv`
2. `virtualenv -p python3.x my_env`  (*replace `python3.x` with any available python verson. Ex: `python3.6`* )
3. Activate virtualenv
    1. **For Ubuntu/Linux** `source my_env/bin/activate`
    2. **For Windows** `\my_env\Scripts\activate.bat`
4. Clone repository `https://github.com/remyaammus/contact-management.git`
5. `cd contact-management/`
6. Install dependencies `pip install -r requirements.txt`
7. Create MYSQL DB
	1. Create new database and export the **necessary**/following env variables ( default values are shown in brackets)
		1. `MYSQL_USER` (`root`)
		2. `MYSQL_PASSWORD` (`password`)
		3. `MYSQL_HOST` (`localhost`)
		4. `MYSQL_PORT` (`5432`)
		5. `MYSQL_DB_NAME` (`my_simple_db`) 
8. `export FLASK_APP='run.py' `
9. migrate the database
10. `flask db upgrade` 
10.  run the app `flask run`
