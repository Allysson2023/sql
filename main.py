import pymysql.cursors

"""
conexao
cursor
"""

try:
    conexao = pymysql.connect(host='localhost', user='root',
                              password='',
                              db='escola',
                              cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida com sucesso!')
except Exception as error:
    print(f'Erro ao estabelecer conexão! Erro: {error}')

# Como criar um cursor?
cursor = conexao.cursor()


def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)
    except Exception as erro:
        print(f'Erro ao buscar os alunos! Erro: {erro}')


def insert(nome, idade, curso, nota):
    try:
        sql = "INSERT INTO alunos (nome, idade, curso, nota) VALUES" \
              "(%s, %s, %s, %s)"
        cursor.execute(sql, (nome, idade, curso, nota))
        conexao.commit()
        print('Aluno cadastrado com sucesso!')
    except Exception as erro:
        print(f'Erro ao cadastrar! Erro: {erro}')


def update(nome, idade, curso, nota, matricula):
    try:
        if verificaAlunoExiste(matricula):
            sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s," \
                  "nota = %s WHERE id = %s"
            cursor.execute(sql, (nome, idade, curso, nota, matricula))
            conexao.commit()
            print('Dados alterados com sucesso!')
        else:
            print('Matricula não encontrada!')
    except Exception as erro:
        print(f'Erro ao atualizar os dados! Erro: {erro}')


def verificaAlunoExiste(id):
    sql = "SELECT * FROM alunos WHERE id = %s"
    cursor.execute(sql, id)
    alunos = cursor.fetchall()
    if len(alunos) == 1:
        return True
    else:
        return False


def delete(id):
    try:
        if verificaAlunoExiste(id):
            sql = "DELETE FROM alunos WHERE id = %s"
            cursor.execute(sql, id)
            conexao.commit()
            print('Dados apagados com sucesso!')
        else:
            print('Matricula não encontrada!')
    except Exception as erro:
        print(f'Erro ao deletar! Erro: {erro}')


delete(4)
select()
