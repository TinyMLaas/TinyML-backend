-- CREATE TABLE sqlite_sequence(name,seq);

CREATE TABLE IF NOT EXISTS "Devices"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name text, 
  connection text, 
  installer text, compiler text, model text, description text
  );
