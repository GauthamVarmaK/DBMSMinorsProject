INSERT INTO manufacturer VALUES('1', 'Lite-On Inc.', 'Building LEDS since 1983, leading producer', 'Mumbai');
INSERT INTO manufacturer VALUES('2', 'Rutherford Tech', 'Building LEDS since 1983, leading producer', 'Kolkata');
INSERT INTO manufacturer VALUES('3', 'TATA Inc.', 'The most trusted Manufacturers', 'Chennai');
INSERT INTO manufacturer VALUES('4', 'MasalaDosaResistors', 'Namma Bengaluru special', 'Bangalore');

INSERT INTO components VALUES('16014451', 'LED ORANGE CLEAR SMD', ' LTST-C191KFKT', '1', 'Orange SMD LED', 'NFNPD', 'LEDS','https://optoelectronics.liteon.com/upload/download/DS22-2000-222/LTST-C191KFKT.pdf', 'Compliant', 'Surface Mount');
INSERT INTO components VALUES('16014452', 'LED GREEN CLEAR SMD', 'LTST-C191KGKT','1','Green SMD LED','NFNPD','LEDS','https://optoelectronics.liteon.com/upload/download/DS22-2000-228/LTST-C191KGKT.PDF','Compliant','Surface Mount');
INSERT INTO components VALUES('16014453', 'LED RED CLEAR SMD', ' LTST-C191KRKT', '1', 'Red SMD LED', 'InProduction', 'LEDS', 'https://optoelectronics.liteon.com/upload/download/DS22-2000-223/LTST-C191KRKT.PDF', 'Compliant', 'Surface Mount');
INSERT INTO components VALUES('16014454', 'LED YELLOW CLEAR SMD', ' LTST-C191KSKT', '2', 'Yellow SMD LED', 'InProduction', 'LEDS', ' https://optoelectronics.liteon.com/upload/download/DS22-2000-224/LTST-C191KSKT.PDF', 'Compliant', 'Surface Mount');
INSERT INTO components VALUES('16014455', 'RESISTOR', 'RTST-S250KGKT', '3', '2.5k SMRA Resistor', 'InProduction', 'LEDS', 'https://optoelectronics.liteon.com/upload/download/DS22-2000-226/LTST-S269KGKT.pdf', 'Compliant', 'Surface Mount Right Angle');
INSERT INTO components VALUES('16014456', 'RESISTOR', 'RTST-S270KGKT', '3', '220 SMD Resistor', 'InProduction', 'Resistors', 'https://optoelectronics.liteon.com/upload/download/DS22-2000-226/RTST-S270KGKT.pdf', 'Compliant', 'Surface Mount');
INSERT INTO components VALUES('16014457', 'RESISTOR', 'RTST-S271CGKT', '4', '45 SMD Resistor', 'InProduction', 'Resistors', 'https://optoelectronics.liteon.com/upload/download/DS22-2000-226/RTST-S271CGKT.pdf', 'Compliant', 'Surface Mount');

INSERT INTO description VALUES('16014451', 'Voltage', '3 Volts');
INSERT INTO description VALUES('16014452', 'Voltage', '3.2 Volts');
INSERT INTO description VALUES('16014453', 'Voltage', '3 Volts');
INSERT INTO description VALUES('16014454', 'Voltage', '1.9 Volts');
INSERT INTO description VALUES('16014455', 'Resistance', '2500 Ohms');
INSERT INTO description VALUES('16014456', 'Resistance', '220 Ohms');
INSERT INTO description VALUES('16014457', 'Resistance', '45 Ohms');

INSERT INTO stock VALUES('16014451',56000,NULL, 'yes');
INSERT INTO stock VALUES('16014457', 402, '2','yes');
INSERT INTO stock VALUES('16014452', 19, '9','yes');
INSERT INTO stock VALUES('16014453', 7, '15' ,'no');
INSERT INTO stock VALUES('16014454', 16, '0','yes');
INSERT INTO stock VALUES('16014455', 26000, '9','yes');
INSERT INTO stock VALUES('16014456', 96754, '9','no');

INSERT INTO price_slabs VALUES('16014451', '50', '2.5');
INSERT INTO price_slabs VALUES('16014451', '500', '2.3');
INSERT INTO price_slabs VALUES('16014451', '5000', '2');
INSERT INTO price_slabs VALUES('16014452', '10', '2.5');
INSERT INTO price_slabs VALUES('16014452', '100', '2.3');
INSERT INTO price_slabs VALUES('16014452', '1000', '2');
INSERT INTO price_slabs VALUES('16014453', '15', '2');
INSERT INTO price_slabs VALUES('16014453', '150', '1.8');
INSERT INTO price_slabs VALUES('16014453', '1500', '1.5');
INSERT INTO price_slabs VALUES('16014454', '40', '1.2');
INSERT INTO price_slabs VALUES('16014454', '400', '1');
INSERT INTO price_slabs VALUES('16014454', '4000', '0.8');
INSERT INTO price_slabs VALUES('16014455', '32', '1.7');
INSERT INTO price_slabs VALUES('16014455', '320', '1.5');
INSERT INTO price_slabs VALUES('16014455', '3200', '1.2');
INSERT INTO price_slabs VALUES('16014456', '30', '2.4');
INSERT INTO price_slabs VALUES('16014456', '300', '2.2');
INSERT INTO price_slabs VALUES('16014456', '3000', '2');
INSERT INTO price_slabs VALUES('16014457', '124', '7');
INSERT INTO price_slabs VALUES('16014457', '1240', '6.5');
INSERT INTO price_slabs VALUES('16014457', '12400', '6');

INSERT INTO users VALUES ('a1', 'Kaushik', 'abc@gmail.com', '8756438291', '2004-02-12','2012-12-12', 'Ulsoor', 'Bangalore', 'Karnataka', '560093');
INSERT INTO users VALUES ('b7', 'Rajesh', 'acd@gmail.com', '8756438671', '2003-02-12','2021-07-12', 'Churchstreet', 'Bangalore', 'Karnataka', '560093');
INSERT INTO users VALUES ('a2', 'Monish', 'eee@gmail.com', '9956438291', '2003-10-10','2023-12-01', 'KumbleCircle', 'Bangalore', 'Karnataka', '560093');
INSERT INTO users VALUES ('a3', 'Nitin', 'dcf@gmail.com', '9956411111', '2000-11-10','2023-12-01', 'RRNagar', 'Bangalore', 'Karnataka', '560012');
INSERT INTO users VALUES ('a4', 'Sajith', 'slv@gmail.com', '6877798222', '2001-11-05','2009-12-12', 'Indiranagar', 'Bangalore', 'Karnataka', '560093');

INSERT INTO orders VALUES('256','a1','2023-04-27', 'Regular', 'ToBeShipped');
INSERT INTO orders VALUES('257','a2','2023-04-01', 'Prime', 'ToBeShipped');
INSERT INTO orders VALUES('258','a3','2020-04-01', 'Prime', 'Delivered');
INSERT INTO orders VALUES('259','a4','2023-04-14', 'BackOrder', 'Shipped');
INSERT INTO orders VALUES('722','b7','2012-04-14', 'Regular', 'Missing');

INSERT INTO order_comp VALUES('256', '16014451', '450');
INSERT INTO order_comp VALUES('257', '16014452', '600');
INSERT INTO order_comp VALUES('258', '16014453', '9000');
INSERT INTO order_comp VALUES('259', '16014454', '200');
INSERT INTO order_comp VALUES('722', '16014457', '1200');

INSERT INTO payments VALUES('130', '256', '5678AB1002', '12000', 'Cash');
INSERT INTO payments VALUES('131', '257', '5678AB1042', '14000', 'Cash');
INSERT INTO payments VALUES('132', '258', '5600AB1342', '25000', 'Cash');
INSERT INTO payments VALUES('133', '259', '5678AB1152', '567', 'UPI');
INSERT INTO payments VALUES('134', '722', '4978AB1152', '20000', 'Cheque');
