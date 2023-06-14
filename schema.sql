CREATE TABLE IF NOT EXISTS "Devices"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT, 
  connection TEXT,
  bridge_id INTEGER, 
  installer_id INTEGER, 
  compiler TEXT, 
  model TEXT, 
  description TEXT, 
  serial TEXT UNIQUE,
  FOREIGN KEY (bridge_id) REFERENCES Bridges (id) ON DELETE CASCADE
  FOREIGN KEY (installer_id) REFERENCES Installers (id) ON DELETE CASCADE
  );
CREATE TABLE IF NOT EXISTS "Bridges"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  ip_address TEXT, 
  name TEXT
  );
CREATE TABLE IF NOT EXISTS "Installers"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT
  );
CREATE TABLE IF NOT EXISTS "Datasets"(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT,
  name TEXT,
  description TEXT
  );
CREATE TABLE IF NOT EXISTS "Models"(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  created TEXT,
  dataset_id INTEGER,
  parameters TEXT,
  description TEXT,
  model_path TEXT,
  FOREIGN KEY (dataset_id) REFERENCES Datasets (id)
  );
CREATE TABLE IF NOT EXISTS "Compiled_models"(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TEXT,
  model_id INTEGER,
  compiler_id INTEGER,
  model_path TEXT,
  FOREIGN KEY (model_id) REFERENCES Models (id),
  FOREIGN KEY (compiler_id) REFERENCES Compilers (id)
  );