INSERT INTO 
  Devices(name, connection, bridge_id, installer_id, model, description, serial)
VALUES
  ('Espressif ESP-EYE', '192.168.1.9', 2, 1, 'person_detection', 'a fine device', '707B266C064B14A6'),
  ('Wio Terminal: ATSAMD51', '192.168.1.11', 2, 1, 'person_detection', 'nice', '707B266C064B14B7'),
  ('STM32F746 Discovery kit', '192.168.1.4', 1, 1, 'mnist_lstm', 'config this', '707B266C064B14C3'),
  ('Commodore 64', '192.168.3.2', 1, 2, 'coffee_detection', 'added new device support', '1985')
;

INSERT INTO 
  Bridges(address, name, https)
VALUES
  ('192.168.0.7', 'Coffee room', 0),
  ('187.32.5.6', 'Parking lot', 0)
;

INSERT INTO
  Datasets(path, name, description)
VALUES
  ('data/cars_dataset/', 'Car recognition', 'Empty rooms vs. pictures of cars'),
  ('data/people_dataset/', 'Person recognition', 'Empty rooms vs. pictures of people'),
  ('data/parking_space_dataset/', 'Free parking space recognition', 'Empty parking space vs. occupied parking space')
;

INSERT INTO
  Installers(name)
VALUES
  ('Arduino IDE'),
  ('RPI')
;