from fastapi import FastAPI, HTTPException, Query
from fastapi_pagination import Page, paginate
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    centro_treinamento = Column(String)
    categoria = Column(String)

app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função utilitária para criar a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo atleta
@app.post("/atletas/")
async def create_atleta(nome: str, cpf: str, centro_treinamento: str, categoria: str, db: Session = Depends(get_db)):
    try:
        db.add(Atleta(nome=nome, cpf=cpf, centro_treinamento=centro_treinamento, categoria=categoria))
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {cpf}")
    return {"nome": nome, "cpf": cpf, "centro_treinamento": centro_treinamento, "categoria": categoria}

# Rota para buscar todos os atletas com paginação
@app.get("/atletas/", response_model=Page[Atleta])
async def get_all_atletas(nome: str = Query(None), cpf: str = Query(None), limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome == nome)
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    atletas = paginate(query, limit, offset)
    return atletas
