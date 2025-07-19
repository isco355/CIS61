#!/bin/bash
clear
 main_file="databases/main.db"

if [ -f $main_file ]; then 

  sqlite3 $main_file < queries/reset_db.sql
  sqlite3 $main_file < queries/main.sql
else
  echo "${main_file} not found(create db file)"
fi


