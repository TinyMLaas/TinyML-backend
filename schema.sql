CREATE TABLE IF NOT EXISTS "Devices"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT, 
  connection TEXT, 
  installer TEXT, 
  compiler TEXT, 
  model TEXT, 
  description TEXT, 
  serial TEXT UNIQUE);
CREATE TABLE IF NOT EXISTS "Bridges"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  ip_address TEXT, 
  name TEXT);
CREATE TABLE IF NOT EXISTS "Compilers"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT);
CREATE TABLE IF NOT EXISTS "Datasets"(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT,
  name TEXT,
  description TEXT);
CREATE TABLE IF NOT EXISTS "Models"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  created TEXT,
  dataset_id INTEGER,
  parameters TEXT,
  description TEXT,
  model_file BLOB,
  FOREIGN KEY (dataset_id) REFERENCES Datasets (id)
  );


