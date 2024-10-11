import os
from sqlalchemy import (
    create_engine, Column, Integer,
    String, Numeric, DateTime,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

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


class Contribuyente(Base):
    """Represents the 'contribuyente' table in the database."""
    __tablename__ = 'contribuyente'
    tipo_contribuyente_id = Column(Integer, primary_key=True)
    tipo_contribuyente = Column(String(45))
    # Relationship with Donantes and Proveedores
    donantes = relationship("Donantes", back_populates="contribuyente")
    proveedores = relationship("Proveedores", back_populates="contribuyente")


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
    tipo_contribuyente_id = Column(
        Integer, ForeignKey(
            'contribuyente.tipo_contribuyente_id', ondelete="CASCADE"))
    cuit = Column(String(20))
    alta = Column(DateTime)
    baja = Column(DateTime)
    activo = Column(String(5))
    frecuencia = Column(String(50))
    importe = Column(Numeric(10, 2))
    nro_cuenta_id = Column(
        Integer, ForeignKey(
            'ingreso_egreso.nro_cuenta_id', ondelete="CASCADE"))
    fecha_donacion = Column(DateTime)

    # Relationship with Contribuyente and Cuenta
    contribuyente = relationship("Contribuyente", back_populates="donantes")
    cuenta = relationship("Cuenta", back_populates="donantes")


class Proveedores(Base):
    """Represents the 'proveedores' table in the database."""
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nro_proveedor = Column(String(50))
    nombre_proveedor = Column(String(50))
    cuit = Column(String(20))
    categoria_proveedor = Column(String(50))
    tipo_contribuyente_id = Column(
        Integer, ForeignKey(
            'contribuyente.tipo_contribuyente_id', ondelete="CASCADE"))
    contacto = Column(String(100))
    correo = Column(String(50))
    telefono = Column(String(20))
    importe = Column(Numeric(10, 2))
    fecha = Column(DateTime)
    nro_cuenta_id = Column(
        Integer, ForeignKey(
            'ingreso_egreso.nro_cuenta_id', ondelete="CASCADE"))
    ciudad = Column(String(50))
    pais = Column(String(50))

    # Relationship with Contribuyente and Cuenta
    contribuyente = relationship("Contribuyente", back_populates="proveedores")
    cuenta = relationship("Cuenta", back_populates="proveedores")


class IngresoEgreso(Base):
    """Represents the 'ingreso_egreso' table in the database."""
    __tablename__ = 'ingreso_egreso'

    nro_cuenta_id = Column(Integer, primary_key=True)
    nro_cuenta = Column(String(20))
    nombre_cuenta = Column(String(50))
    tipo_cuenta = Column(String(50))
    descripcion = Column(String(255))

    # Relationship with Donantes and Proveedores
    donantes = relationship("Donantes", back_populates="cuenta")
    proveedores = relationship("Proveedores", back_populates="cuenta")


# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Close the session at the end
session.close()
