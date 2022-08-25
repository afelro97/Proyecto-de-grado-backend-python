from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

meta = MetaData()

conn = engine.connect()