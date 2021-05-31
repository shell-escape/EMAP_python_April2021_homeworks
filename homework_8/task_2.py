"""
Preamble
========

We have a database file (example.sqlite) in sqlite3 format with some
tables and data. All tables have 'name' column and maybe some
additional ones.

Data retrieval and modifications are done with sqlite3 module by
issuing SQL statements.

For example, to get all data from TABLE1::

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from TABLE1')
    data = cursor.fetchall()   # will be a list with data.

instead of getting all data at once, you can use .fetchone()
calls and named expressions::

    while row:=cursor.fetchone():
        print(row)

To get a row with specific name equal to some value::

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from presidents where name=:name',
                   {name:'Yeltsin'})
    data = cursor.fetchall() # will get all records with this name.
    # You can also use .fetchone() to get one record.

in order to get record with first name (sorted alphabetically) use SQL
expression `SELECT * from presidents order by name asc limit 1`
in order to get record after specified (sorted alphabetically) use SQL
expression `SELECT * from presidents where name >
            :name order by name limit`.
To get amount of records in table TABLE1, use
`select count(*) from TABLE1` query.


Please refer to this documents for more information about how to
retrieve data from sqlite database:
DBAPI: https://www.python.org/dev/peps/pep-0249/
sqlite3 module: https://docs.python.org/3/library/sqlite3.html


Task
====

Write a wrapper class TableData for database table, that when
initialized with database name and table acts as collection
object (implements Collection protocol).

Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite',
                              table_name='presidents')

then
 -  `len(presidents)` will give current amount of rows
                      in presidents table in database
 -  `presidents['Yeltsin']` should return single data
                            row for president with name Yeltsin
 -  `'Yeltsin' in presidents` should return if president
                              with same name exists in table
 -  object implements iteration protocol. i.e. you could use
    it in for loops::
       for president in presidents:
           print(president['name'])
 - all above mentioned calls should reflect most recent data.
   If data in table changed after you created collection
   instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records,
start reading the first record, then go to the next one, until records
are exhausted.
When writing tests, it's not always neccessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file.
"""

import sqlite3
from contextlib import contextmanager
from typing import Any, ContextManager, Generator


class InjectionError(Exception):
    """Exception that raises when table name is not valid"""

    pass


class TableData:
    """Class for database table that acts like collection object.

    Args:
        database_name: database name.
        table_name: table name.

    Attributes:
        database_name: database name.
        table_name: table name.
    """

    def __init__(self, database_name: str, table_name: str):
        if not table_name.isidentifier():
            raise InjectionError("Table name is not valid.")
        self.database_name = database_name
        self.table_name = table_name

    @contextmanager
    def connection(self) -> ContextManager:
        """Context manager for sqlite3 connection."""

        con = sqlite3.connect(self.database_name)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        yield cur
        con.commit()
        con.close()

    def __len__(self) -> int:
        with self.connection() as cursor:
            cursor.execute(f"SELECT count(*) as len FROM {self.table_name}")  # noqa
            return cursor.fetchone()["len"]

    def __getitem__(self, item: str) -> Any:
        with self.connection() as cursor:
            command = f"SELECT * FROM {self.table_name} WHERE name=:name"  # noqa
            cursor.execute(command, {"name": item})
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"There is no item {item}")
            return result

    def __contains__(self, item: str) -> bool:
        try:
            return bool(self[item])
        except ValueError:
            return False

    def __iter__(self) -> Generator:
        with self.connection() as cursor:
            yield from cursor.execute(f"SELECT * from {self.table_name}")  # noqa
