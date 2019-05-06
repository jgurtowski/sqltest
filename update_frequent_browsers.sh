#!/bin/bash

# Delete existing data from frequent browsers
# then update the table with the new top 10 frequent browers

sqlite3 testdb.db <<EOF
	delete from frequent_browsers;
	insert into frequent_browsers select personId,count(*) as vcount from visits group by personId order by vcount desc limit 10; 
EOF


