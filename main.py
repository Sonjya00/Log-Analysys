# !/usr/bin/env python

import psycopg2

''' Queries to check'''

# 1. What are the most popular three articles of all time?
query_1_msg = "The most popular three articles of all time are:\n"
query_1 = '''SELECT articles.title, count(*) AS views
           FROM articles, log
           WHERE log.path = concat('/article/', articles.slug)
           GROUP BY articles.title
           ORDER BY views DESC limit 3'''
query_1_unit = " views"

# 2. Who are the most popular article authors of all time?
query_2_msg = "The most popular article authors of all time are:\n"
query_2 = '''SELECT authors.name, count(*) AS views
           FROM authors, articles, log
           WHERE articles.author = authors.id
           AND log.path = concat('/article/', articles.slug)
           GROUP BY authors.name
           ORDER BY views DESC'''
query_2_unit = " views"

# 3. On which days did more than 1% of requests lead to errors?
query_3_msg = "The day when more than 1% of requests lead to errors is:\n"
query_3 = '''SELECT * FROM
                (SELECT to_char(log.time, 'fmMonth DD, YYYY') AS date,
                round(100.0 *
                sum(case log.status when '200 OK' then 0 else 1 end)
                /count(log.status), 2) AS error_rate
                FROM log
                GROUP BY date
                ORDER BY error_rate DESC)
            AS subq
            WHERE error_rate > 1'''
query_3_unit = "% errors"

'''Getting results from queries and displaying them'''


def get_results(query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def print_results(query, query_msg, query_unit):
    results = get_results(query)
    print(query_msg)
    for result in results:
        print("{} - {}{}".format(str(result[0]), str(result[1]), query_unit))
    print("\t")


if __name__ == "__main__":
    print_results(query_1, query_1_msg, query_1_unit)
    print_results(query_2, query_2_msg, query_2_unit)
    print_results(query_3, query_3_msg, query_3_unit)
