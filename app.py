from flask import Flask, render_template, request #até aqui, já tinhamos visto tudo
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from models.seu_modelo import * #Importando o nosso modelo de classe que será uma tabela no banco de dados
from utilidades import * #Importando a instância do banco de dados lá no arquivo utilidades


app = Flask(__name__) #Criando o app Flask

load_dotenv() #Carrega variáveis do nosso arquivo .flaskenv

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env


conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Criando uma "rota" de comunicação
db.init_app(app) #Sinaliza que o banco será gerenciado pelo app


#Rotas:

@app.route('/', methods = ["get","post"])
def inicio():
    return render_template("XXXX.html")