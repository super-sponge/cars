truncate table cars;
LOAD DATA LOCAL INFILE '/tmp/cars_load.csv'
INTO TABLE cars
character set utf8  
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
lines terminated by '\r\n'
ignore 1 lines
(carName,carId,engine,gearbox,lwh,bodywork,maxSpeed,sits,fuelForm,gearboxName,gearboxblocks,gearboxType); 
