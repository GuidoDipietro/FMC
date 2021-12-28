######  Generates SQL table from FMC solutions .txt file ######
######               Guido Dipietro - 2021               ######
import mysql.connector

## DB connection
DB_NAME = "fmc_dataset"
DB_PWD = ""
with open("../data/db_pwd.txt", "r") as f:
	DB_PWD = f.read()

db = mysql.connector.connect(host="127.0.0.1",user="root",password="navarro",database=DB_NAME)

## Gathering FMC solutions data
DATA_FILENAME = "__FMC.txt"
data = ""
with open(f"../data/{DATA_FILENAME}", "r") as f:
	data = f.read()

data_arr = data.split("---")

print(data_arr)
print(len(data_arr))
