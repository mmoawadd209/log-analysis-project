﻿# LOGS ANALYSIS PROJECT - Udacity FSDN



The project requires creating a reporting tool that fetchs results from a large database of a "NEWS" website and prints out
reports(in plain text) based on the data in the given database.

The database includes three tables:
* authors table contains information about the authors of articles.
* articles table contains information about the articles.
* log table has a database row for each time a reader loaded a web page.

The Python script uses the psycopg2 library to query and produce a report that answers the following questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?


### Prerequisites

* [Python3](https://www.python.org) - The code uses ver 3.6.4
* [Vagrant](https://www.vagrantup.com) - A virtual environment builder and manager
* [VirtualBox](https://www.virtualbox.org) - An open source virtualiztion product
* [Udacity_Preconfigured_VM](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) Alternately, you can use Github to fork and clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository.
* Udacity [“news”](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)   Database File.


### Installing

* Download and install Python.
* Download and install Vagrant and VirtualBox.
* Download this Udacity folder with preconfigured vagrant settings.
* Download data provided by Udacity 	
* Unzip file to extract newsdata.sql This file should be inside the Vagrant folder.
* Open a terminal windows and navigate to your VM folder Vagrant.
* Use Commands 'vagrant up' to start the VM and'vagrant ssh' to connect to it. 
* cd to /vagrant shared folder.
* Load the database using 'psql -d news -f newsdata.sql'
* connect to the database using 'psql -d news'. 
* create the following views:
    
    * popular_articles
    
      create or replace view popular_articles as
      select articles.title, count(*) as count
            from log, articles
            where log.path = concat('/article/',articles.slug)
            and log.status='200 OK'
            group by articles.title
            order by count desc
      
    * popular_authors
    
      create or replace view popular_authors as
      select authors.name, count(*) as count
            from articles, authors, log
            where authors.id = articles.author
            and log.path = concat('/article/',articles.slug)
            and log.status='200 OK'
            group by authors.name
            order by count desc
    
    * request_errors
    
      create or replace view request_errors as
      select errors_count.date, errors_count.errors, time_count.total
            from (select time::date as date, count() as errors 
            from log where status!='200 OK' 
            group by date) as errors_count
            join (select time::date as date, count() as total
            from log
            group by date) as time_count
            on errors_count.date=time_count.date
            order by errors_count.date asc);

## Running the tool

* Open a terminal windows and navigate to your VM folder Vagrant.
* Use Commands 'vagrant up' to start the VM and 'vagrant ssh' to connect to it.
* cd to /vagrant folder.
* execute the Python file using 'python report-results.py'.	
