# Log Analysis Project

## Project Description

This is a project made for the completion of the Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Instructions

Create a reporting tool that prints out reports (in plain text) based on the data inside of the database of a fictional newspaper site. The database contains details about each article and article author, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The program runs from the command line without taking any input from the user. Instead, it connects to the database, uses SQL queries to analyze the log data, and prints out the answers to the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How to start

1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html). Make sure you have the latest version of [Python](https://www.python.org/download/releases/3.0/) installed;
2. Download this repository and cd into it in the terminal;
3. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it and place the file newsdata.sql into the repository;
4. On the terminal, input `vagrant up` to launch the virtual machine, then `vagrant ssh` to continue;
5. Input `cd /vagrant`;
6. Load the database using `psql -d news -f newsdata.sql`;
7. Start running the queries with the command `python main.py`;

The terminal will then start displaying the results to the questions previously listed.
