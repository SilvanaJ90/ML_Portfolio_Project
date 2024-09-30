-- create database --
CREATE DATABASE "funds_management";
-- create role --
create role "funds_management" with password 'pass123';
-- Grant login permissions --
alter role "funds_management" with login;


-- grants roles -----
\c "funds_management";
GRANT USAGE ON SCHEMA public TO "funds_management";
GRANT CREATE ON SCHEMA public TO "funds_management";
GRANT CONNECT ON DATABASE "funds_management" TO "funds_management";
GRANT ALL PRIVILEGES ON DATABASE "funds_management" TO "funds_management";


-- Grant CRUD permissions --
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE ' || quote_ident(r.tablename) || ' TO funds_management';
    END LOOP;
END $$;

GRANT ALL PRIVILEGES ON DATABASE funds_management TO funds_management;


-- assigning the tables to the database user
ALTER TABLE donantes owner to "funds_management";
ALTER TABLE proveedores owner to "funds_management";
ALTER TABLE  ingreso_egreso owner to "funds_management";