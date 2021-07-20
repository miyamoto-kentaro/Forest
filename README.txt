############# db #############
$ psql
-> login
user-# \l
-> db list

$ psql -d ForestDB
ForestDB=# \conninfo
and cp /var/run/postgresql:5432

$ export DATABASE_URL="postgresql:///ForestDB"

起動
$ sudo service postgresql start
ストップ
$ sudo service postgresql stop
''