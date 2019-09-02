# !/usr/bin/env python

import psycopg2

DBNAME = "news"

articles_query = " SELECT * FROM popular_articles LIMIT 3;"

authors_query  = " SELECT * FROM popular_authors;"

errors_query   = (""" SELECT to_char(date, 'TMMonth DD"," YYYY'),count
                      FROM request_errors
                      WHERE count > 1.0;""")


def execute_query(sql_query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
            
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

popular_articles = execute_query(articles_query)
popular_authors = execute_query(authors_query)
request_errors = execute_query(errors_query)



def print_results(query_result):
    for i in range(len(query_result)):
        title = query_result[i][0]
        count = query_result[i][1]
        print("\t" + "%s - %d" % (title, count) + " views")
    print("\n")

print("What are the most popular articles of all time?")
print_results(popular_articles)
print("Who are the most popular article authors of all time?")
print_results(popular_authors)
print("On which days more than 1% of the requests led to error?")
print("\t" + date + " - " + str(count) + "% errors\n")
