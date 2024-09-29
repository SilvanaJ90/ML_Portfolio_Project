import os
from sqlalchemy import (
    create_engine, Column, Integer,
    String, BigInteger, Numeric,
    DateTime, ForeignKey
    )
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from dotenv import load_dotenv


load_dotenv()
# Get environment variables
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Create the database engine
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Donantes(Base):
    """Represents the 'donantes' table in the database."""
    __tablename__ = 'donantes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(String(50))
    nombre = Column(String(50))
    tipo = Column(String(50))
    contacto = Column(String(50))
    correo = Column(String(50))
    telefono = Column(String(20))
    observaciones = Column(String(100))
    tipo_contribuyente = Column(String(50))
    cuit = Column(String(20))
    alta = Column(DateTime)
    baja = Column(DateTime)
    activo = Column(String(5))
    frecuencia = Column(String(50))
    importe = Column(Numeric(10, 2))
    nro_cuenta = Column(BigInteger)
    fecha_donacion = Column(DateTime)


class Proveedores(Base):
    """Represents the 'proveedores' table in the database."""
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_proveedor = Column(String(50))
    nombre_proveedor = Column(String(50))
    cuit = Column(String(20))
    categoria_proveedor = Column(String(50))
    tipo_contribuyente = Column(String(50))
    contacto = Column(String(100))
    correo = Column(String(50))
    telefono = Column(String(20))
    importe = Column(Numeric(10, 2))
    fecha = Column(DateTime)
    nro_cuenta = Column(BigInteger)
    ciudad = Column(String(50))
    pais = Column(String(50))


class IngresoEgreso(Base):
    """Represents the 'ingreso_egreso' table in the database."""
    __tablename__ = 'ingreso_egreso'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_cuenta = Column(BigInteger)
    nombre_cuenta = Column(String(50))
    tipo_cuenta = Column(String(50))
    descripcion = Column(String(255))


# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Log out at the end
session.close()
