Load Troy Hunt blacklisted password data set in dynamoDB
========================================================

Steps:
------

    * Download Troy Hunt data set which is around 9 GB.
    * Extract downloaded file (will be around 22 GB). 
    * Split single file to manage it better in 500 MB files.
    * Prune or trim data to pick passwords which were compromised more then configurable threshold number. 
    * Load data batches in dynamoDB using python script. 
    * This script loads data and assumes that expected table already exists before you run it. 


Download Troy Hunt data set:
===========================

    https://haveibeenpwned.com/Passwords
    SHA-1	Version 3 (ordered by hash)	13 Jul 2018	9.18GB	10c001292d52a04dc0fb58a7fb7dd0b6ea7f7212

Extract data:
============

    Extract / unzip the file, it will provide a single 22 GB file. 
    Each line of file woould look like 
    20EABE5D64B0E216796E834F52D61FD0B70332FC:2298084 

Split single file:
=================

    Split single file to manage it better in 500 MB files 
    $ split -b <size in bytes> sourceFilePath splittedFilesPath
    eg. split -b 26214400 pwned-passwords-ordered-by-hash.txt ./splitedFiles/blacklist
    
Prune or trim data
==================
   
    # configure threshold value in var
    THRESHOLD_LIMIT=5000
    
    # use gawk command to prune or trim file (install gawk package if required)

    $ gawk 'BEGIN {FS=":"} {if($2>'$THRESHOLD_LIMIT') {print $1":"$2 } }' sourceFile > sourceFile-pruned.txt
    eg. gawk 'BEGIN {FS=":"} {if($2>'$THRESHOLD_LIMIT') {print $1":"$2 } }' blacklistFile > blackListFile-pruned.txt
    
Move pruned file
================
    
    Validate all files are pruned or trimmed or filtered based on threshold limit.
    Once all files are pruned, move them to a folder so that it can be used as input for data loader script.
    $ mkdir -p ./prunedInputFile
    eg. mv *-pruned.txt ./prunedInputFile 
    
Configure AWS dynamoDb details
==============================
    please provide details in `config.properties` and logging levels in `logging.properties`
    These files are located in resources folder. The default relative path would look like:
    ./resources/config.properties
    ./resources/logging.properties
    
    Custom location of above configuraiton can be passed using the optional flag or argument to the script
    -c for path of config.properties
    -l for path of logging.properties

    Note: It is assumed that aws configs are already set in ~/.aws folder with `aws_secret_access_key` and id

Sample config.properties
=======================    
    [dynamodb]
    endpoint_url = http://localhost:8000
    region = us-west-2
    table_name = password_blacklist
    
Sample logging.properties
=======================  
    [loggers]
    keys=root
    
    [handlers]
    keys=console
    
    [formatters]
    keys=simple
    
    [logger_root]
    handlers=console
    level=INFO
    
    [handler_console]
    class=StreamHandler
    formatter=simple
    args=(sys.stdout,)
    
    [formatter_simple]
    format=%(asctime)s %(levelname)s %(message)s
    class=logging.Formatter
    
Create table in dynamoDb
========================

    Table could be created using web console ( better control) 
    
    Below command can be used to create table using SDK
    TABLE_NAME=pwd_blacklist
    KEY_NAME=pwd_hash
    
    $ aws dynamodb create-table --table-name $TABLE_NAME --attribute-definitions AttributeName=$KEY_NAME,AttributeType=S  --key-schema AttributeName=$KEY_NAME,KeyType=HASH  --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000
    
    # Validate if table is created before inserting data
    $ aws dynamodb list-tables --endpoint-url http://localhost:8000
    
Inserting data in DynamoDB
==========================

    Please make sure, you have python 3 enviornment and load required pip modules
    $ pip install requirements.txt 
    
    $ python data_loader.py -f <path of data file with troy password data set>
    eg. python data_loader.py -f /Users/asee2278/dataloding/demo/splitedFiles/prunedInputFile/blacklistaa-pruned.txt 
    
    Optionally path of config and logging can be passed as arguments as well 
    eg. python data_loader.py -f ~/input.txt -c ~/myconfig.properties -l ~/mylogging.preperties

Consolidated report 
===================
    At the end of script you will see a consolidated report like below:
    
    /Users/asee2278/virtualEnvironments/p2/bin/python /Users/asee2278/idmCode/aseemFork/cloud-identity-client-scripts/dynamodb_scripts/data_loader.py -f input.txt
    2018-10-09 20:48:09,975 INFO ***** Consolidated report of data insertion for the input file input.txt
    2018-10-09 20:48:09,975 INFO Number of records 35000
    2018-10-09 20:48:09,975 INFO Number of records inserted 35000
    2018-10-09 20:48:09,975 INFO Number of records failed to insert 0




aws dynamodb list-tables --endpoint-url https://dynamodb.us-east-2.amazonaws.com

