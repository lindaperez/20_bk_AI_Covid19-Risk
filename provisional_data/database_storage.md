# Database Storage 

## AWS

AWS is a cloud computing environment that provides lots of services required for most of the applications developed nowadays.

## RDS

Amazon Relational Database Service (RDS) is a managed SQL database service provided by Amazon Web Services (AWS) that supports an array of database engines to store and organize data. It also helps with relational database management tasks, such as data migration, backup, recovery, and patching.

## Relational Database

The decision of creating a Relational database was based on the sources found, 

1. Free-Tier AWS:  the cost of processing and storing is free for most of the requirements. 
2. Team developers: have a better understanding of relational databases which will not be going to incur additional time for learning.
3. The expected operation over the database is mainly read.

## ERD - SCHEMA

Is located in [ERD schema](https://github.com/lindaperez/bk-covid19/blob/main/provisional_data/ERD/schema/schema_backup)

## Colaborative Enviroments

Latest environment from where it is exported the ERD

Sample db with 3500000 over around 16 million
Endpoint: prod-covid-patients.cqbgcjbaetrj.us-west-1.rds.amazonaws.com
username: postgres
database: covid_db

* sample environment 

- Sample db with 100000
- Endpoint: prodsamplecovidpatients.cqbgcjbaetrj.us-west-1.rds.amazonaws.com
- username: postgres
- database: sample_covid_patients


* mock environment 

- Endpoint: covidpatients.cqbgcjbaetrj.us-west-1.rds.amazonaws.com
- username: postgres
- database: covid_patients





