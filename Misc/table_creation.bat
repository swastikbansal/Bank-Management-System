@echo off

echo Creating Table

set /p password= Enter your Password (mysql login) : 

mysql -uroot -p%password% < "banking_migration_script.sql"

echo Table Created Successfully!!

PAUSE