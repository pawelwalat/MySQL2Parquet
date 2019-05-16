# MySQL2Parquet
Simple tool to dump data from Mysql DB to Parquet format

Tool tested on Python 3.6.2 (Linux) and 3.7.3 64-bit (Windows)

Prerequisites:
pip install mysql
pip install pandas
pip install pyarrow

2 Options to chose:
Option A) (hard)
install snappy library
pip install python-snappy
Option B) (easy)
Download python_snappy-0.5.4-cp37-cp37m-win_amd64.whl from: http://google.github.io/snappy/
pip install python-snappy python_snappy-0.5.4-cp37-cp37m-win_amd64.whl
(file name my change dependin on OS and snappy version)

How to use:
python Mysql2Parquet.py output_filename mysql_host mysql_user mysql_password "select_statement"