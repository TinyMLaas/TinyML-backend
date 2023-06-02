INSERT INTO 
  Devices(name, connection, installer, compiler, model, description, serial)
VALUES
  ("Espressif ESP-EYE", "192.168.1.9", "Arduino IDE", "TFLiteConverter", "person_detection", "a fine device", "707B266C064B14A6"),
  ("Wio Terminal: ATSAMD51", "192.168.1.11", "Arduino IDE", "TFLiteConverter", "person_detection", "nice", "707B266C064B14B7"),
  ("STM32F746 Discovery kit", "192.168.1.4", "Arduino IDE", "TFLiteConverter", "mnist_lstm", "config this", "707B266C064B14C3"),
  ("Commodore 64", "192.168.3.2", "Commodore Basic", "TFLiteToC64", "coffee_detection", "added new device support", "1985")
;

INSERT INTO 
  Bridges(ip_address, name)
VALUES
  ("192.168.0.7", "Coffee room"),
  ("187.32.5.6", "Parking lot")
;