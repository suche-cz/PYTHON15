"""
databáze: DB Browser SQLite (client)
Příklady Relačních DB systémů: MySQL, PostgreSQL, Oracle, SQLite, MS SQL Server

Základní DB objekt: Tabulka
- řádky - definuje záznamy (instance)
- sloupce - definuje vlastnosti (atributy, informace o záznamu)
    - datové typy


SQL - Structured Query Language

Data Definition Language (DDL)
- create table
- update table
- drop table

Data Manipulation Language (DML)
- insert
- update
- delete

Data Query
- select

SQL Joiny
SQL Indexy
SQL Inject - bezpečnostní riziko, vždy používat jako parametry (Django to má vyřešené)

DB transakce - pokud příkazy provedeme v 1. transakci vykonají se všechny nebo žádná
- např může nastat chyba (ostatní se neprovede a předohozí se vrátí do původního stavu - rollback)

druhy databází
relační - mají pevně danou struktury a vztahy - tabulky a vazby pomocí cizích klíčů
objektová - uložení dat ve formě json objektů
"""

import sqlite3

# 1. Připojení (vytvoří soubor pokud neexistuje)
conn = sqlite3.connect('shop.db') # connection - spojení s DB
cursor = conn.cursor() # cursor - rozhraní pro ovládání DB

# 2. DDL: Vytvoření tabulky
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL
    )
''')

# 3. DML: Insert (vložení dat)
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ('Káva', 45.0))

# 4. DQL: Select (výběr dat)
cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. TCL: Potvrzení změn a uzavření
conn.commit()
conn.close()
