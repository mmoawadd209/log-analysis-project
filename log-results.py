# !/usr/bin/env python

import psycopg2

DBNAME = "news"

firstQuery = ("SELECT title, count(*) as views FROM articles \n"
           "  JOIN log\n"
           "    ON articles.slug = substring(log.path, 10)\n"
           "    GROUP BY title ORDER BY views DESC LIMIT 3;")

secondQuery = ("SELECT authors.name, count(*) as views\n"
           "    FROM articles \n"
           "    JOIN authors\n"
           "      ON articles.author = authors.id \n"
           "      JOIN log \n"
           "      ON articles.slug = substring(log.path, 10)\n"
           "      WHERE log.status LIKE '200 OK'\n"
           "      GROUP BY authors.name ORDER BY views DESC;")

thirdQuery = ("SELECT round((stat*100.0)/visitors, 3) as\n"
           "        result, to_char(errortime, 'Mon DD, YYYY')\n"
           "        FROM errorcount ORDER BY result desc limit 1;")


def get_queryResults(sql_query):
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

result1 = get_queryResults(firstQuery)
result2 = get_queryResults(secondQuery)
result3 = get_queryResults(thirdQuery)



def print_results(query_list):
    for i in range(len(query_list)):
        title = query_list[i][0]
        r = query_list[i][1]
        print("\t" + "%s - %d" % (title, r) + " views")
    print("\n")

print("What are the most popular articles of all time?")
print_results(result1)
print("Who are the most popular article authors of all time?")
print_results(result2)
print("On which days more than 1% of the requests led to error?")
print("\t" + result3[0][1] + " - " + str(result3[0][0]) + "%")
