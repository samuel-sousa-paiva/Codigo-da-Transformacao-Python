import sqlite3

conn = sqlite3.connect('atividade_info_cliente.db')

cursor = conn.cursor()


cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )

''')

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('Matheus Hideo', 'joao.silva@mail.com'),
               
    ('Antônio  Alves', 'maria.oliveira@mail.com'),
               
    ('Alexandra Augusta ', 'carlos.santos@mail.com'),
               
    ('Lucas Freitas', 'joao.silva@mail.com'),
               
    ('Arthur Augusto ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('Jhonatas nascimento', 'joao.silva@mail.com'),
               
    ('Antônio  Alberto', 'maria.oliveira@mail.com'),
               
    ('Alex Augustinho ', 'carlos.santos@mail.com'),
    
    ('Adriana Almeida', 'joao.silva@mail.com'),
               
    ('Angélica Andrade', 'maria.oliveira@mail.com'),
               
    ('Alê Alvarenga', 'carlos.santos@mail.com')
               

''')

conn.commit()