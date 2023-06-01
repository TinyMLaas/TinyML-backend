CREATE TABLE IF NOT EXISTS "Devices"(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, connection text, installer text, compiler text, model text, description text, serial text);
CREATE TABLE IF NOT EXISTS "Bridges"(id INTEGER PRIMARY KEY AUTOINCREMENT, ip_address text, name text);
