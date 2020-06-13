#!/usr/bin/env python3

##########################################################################
### Mysql2Parquet
### Author: Pawel Walat
### Current Version: 1.0
###
### Change Log:
###     1.0: 15-May-2019 - Initial version (Pawel Walat)
###     1.1: 12-Jun-2020 - Adding DB name parameter
##########################################################################

import MySQLdb as dbapi
import sys
import csv
import pandas as pd


if len(sys.argv) != 7: 
    sys.exit('Usage: '+sys.argv[0]+' [output_file] [hostname/ip] [username] [password] [db_name] "[select statement]"')

output_file = sys.argv[1]
hostname 	= sys.argv[2]
username 	= sys.argv[3]
password 	= sys.argv[4]
db_name 	= sys.argv[5]
select 		= sys.argv[6]


try:
	db=dbapi.connect(hostname,username,password,db_name)
	cur=db.cursor()
	cur.execute(select)
	result=cur.fetchall()	
except (dbapi.Error, dbapi.Warning) as e:
	print("Error: "+str(e))	
	sys.exit(1)

try:
	field_names = [i[0] for i in cur.description]
	df = pd.DataFrame(list(result), columns=field_names)
	df.to_parquet(output_file)
	print("File \""+output_file+"\" saved successfully!")	
except:
	print("Error: "+sys.exc_info()[0])
	
