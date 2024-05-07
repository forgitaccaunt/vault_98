import sqlite3


with sqlite3.connect('Databases/vault_98.db') as connection:
    cursor = connection.cursor()

    try:
        with connection:
            query = '''INSERT INTO Games (name, info)
            VALUES
            ("VAULT-Quote", "Случайная цитата из мира до Ядерной войны"),
            ("VAULT-Quiz", "Викторина обо всём!"),
            ("ARCADA", "Увлекательная аркада с пушками")
            '''
            cursor.execute(query)
    except Exception:
        print("TERMINAL ERROR")
