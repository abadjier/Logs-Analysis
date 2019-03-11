# Python 3 script

import psycopg2

DBNAME = "news"

# connect to database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


# Query for most popular three articles
query1 = ("select a.title, b.num "
          "from articles a, "
          "(select regexp_replace(path, '^.+[/]', '') as slug, "
          "count(*) as num "
          "from log where path like '%article%' "
          "group by path order by num desc limit 3) b "
          "where a.slug = b.slug "
          "order by b.num desc")

# Query for most popular article authors
query2 = ("select au.name, totals_tbl.num "
          "from authors au, "
          "(select a.author, sum(s_tbl.num_each) as num "
          "from articles a, "
          "(select regexp_replace(path, '^.+[/]', '') as slug, "
          "count(*) as num_each "
          "from log where path like '%article%' group by path) s_tbl "
          "where a.slug=s_tbl.slug "
          "group by a.author order by num desc) totals_tbl "
          "where au.id = totals_tbl.author")

# Query for days with more than 1% of error requests
query3 = ("select date, percent "
          "from (select date, round( 100.0 * (ct/total), 2) as percent "
          "from (select status, date, ct, "
          "sum(ct) over (partition by date) as total "
          "from (select status, count(status) as ct, time::date as date "
          "from log group by time::date, status) "
          "as counts_table) "
          "as totals_table where status not like '%2%') "
          "as percent_table where percent>1")

c.execute(query1)
answer1 = c.fetchall()

# execute query2 and then fetch into answer2
c.execute(query2)
answer2 = c.fetchall()

# execute query3 and fetch into answer3
c.execute(query3)
answer3 = c.fetchall()

# close connection to database
db.close()

# create and open a text file to write in the program output
f = open("answers.txt", "w+")

# using the write function enter query results into the text file answers.txt
f.write("Question 1.\r\n "
        " What are the most popular three articles of all time?"
        "\r\n Answer:\r\n")
for i in range(len(answer1)):
    f.write("  \"{}\" - {} views\r\n".format(answer1[i][0], answer1[i][1]))

f.write("\r\nQuestion 2.\r\n "
        " Who are the most popular article authors of all time?"
        "\r\n Answer:\r\n")
for i in range(len(answer2)):
    f.write("  {} - {} views\r\n".format(answer2[i][0], answer2[i][1]))

f.write("\r\nQuestion 3.\r\n "
        "On which days did more than 1% of requests lead to errors?"
        "\r\n Answer:\r\n")
for i in range(len(answer3)):
    f.write(
        "  {} - {}% errors\r\n".format(
            answer3[i][0].strftime('%B %d, %Y'), answer3[i][1]))

# close .txt file
f.close()
