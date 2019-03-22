# !/usr/bin/env python

import psycopg2

''' Queries to check'''

# 1. What are the most popular three articles of all time?
query_1_msg = "The most popular three articles of all time are:\n"
query_1 = ("select articles.title, count(*) as views "
           "from articles, log "
           "where log.path = concat('/article/', articles.slug) "
           "group by articles.title "
           "order by views DESC limit 3")

# 2. Who are the most popular article authors of all time?
query_2_msg = "The most popular article authors of all time are:\n"
query_2 = ("select authors.name, count(*) as views "
           "from authors, articles, log "
           "where articles.author = authors.id "
           "and log.path = concat('/article/', articles.slug) "
           "group by authors.name "
           "order by views DESC")

# 3. On which days did more than 1% of requests lead to errors?
query_3_msg = "The day when more than 1% of requests lead to errors is:\n"
# query_3 = ("select * from log ")

'''Getting results from queries and displaying them'''


def get_results(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def print_results(query, query_msg):
    results = get_results(query)
    print(query_msg)
    for result in results:
        print("{} - {}".format(str(result[0]), str(result[1])))
    print("\t")

print_results(query_1, query_1_msg)
print_results(query_2, query_2_msg)
print_results(query_3, query_3_msg)
