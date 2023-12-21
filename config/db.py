from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker

# engine=create_engine('mysql+mysqlconnector://root:12345678@34.142.199.170:3306/artiquest_database')
engine=create_engine('mysql+mysqlconnector://root:@localhost:3306/artiquest_database')

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# con = SessionLocal()

meta=MetaData()
con=engine.connect()
