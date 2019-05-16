#!/usr/bin/env python3

##########################################################################
### Mysql2Parquet
### Author: Pawel Walat
### Current Version: 1.0
###
### Change Log:
###     1.0: 15-May-2019 - Initial version (Pawel Walat)
##########################################################################

import MySQLdb as dbapi
import sys
import csv
import pandas as pd


if len(sys.argv) != 6: 
    sys.exit('Usage: '+sys.argv[0]+' [output_file] [hostname/ip] [username] [password] "[select statement]"')

output_file = sys.argv[1]
hostname 	= sys.argv[2]
username 	= sys.argv[3]
password 	= sys.argv[4]
select 		= sys.argv[5]


try:
	db=dbapi.connect(host=hostname,user=username,passwd=password)
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
except:
	print("Error: "+sys.exc_info()[0])

print("File \""+output_file+"\" saved successfully!")	
	