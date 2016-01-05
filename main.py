#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from scrapy import cmdline
import csv, os


def filtercsv(filein, fileout, fields):
    firstRow = True
    index = []
    csv.field_size_limit(831072)
    if not os.path.isfile(filein):
        return
    with open(filein, 'rb') as fin:
        with open(fileout, 'wb') as fout:
            writer = csv.writer(fout)
            for line in csv.reader(fin):
                if firstRow:
                    firstRow = False
                    for field in fields:
                        index.append(line.index(field))
                if (len(line) < max(index)):
                    print 'error ' + " ".join(line)
                    continue
                row = []
                for i in index:
                    row.append(line[i])
                # row = line[index]
                writer.writerow(row)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl autohome'.split())
    filtercsv('/home/sponge/scrapy/cars/data/cars.csv', '/home/sponge/scrapy/cars/data/cars_field.csv',
              ['name',
               'prices',
               'factory',
               'level',
               'engine',
               'gearbox',
               'lwh',
               'bodywork',
               'maxSpeed',
               'acceleration100',
               'trueAcceleration100',
               'brake',
               'fuelConsumption',
               'MFuelConsumption',
               'groundClearance',
               'vehicleWarranty',
               'length',
               'wide',
               'high',
               'wheelbase',
               'frontGauge',
               'backGauge',
               'MinimumGroundClearance',
               'kerbMass',
               'bodywork',
               'doors',
               'sits',
               'fuelCapacity',
               'LuggageCapacity',
               'engineType',
               'displacement',
               'airIntakeForm',
               'cylinderArrangement',
               'cylinders',
               'valvesPerCylinder',
               'compressionRatio',
               'valveActuatingMechanism',
               'bore',
               'stroke',
               'maximumHorsepower',
               'maximumPower',
               'maximumPowerSpeed',
               'maxTorque',
               'maximumTorqueSpeed',
               'engineSpecifictechnology',
               'fuelForm',
               'fuelLabel',
               'oilSupplyMode',
               'cylinderHeadMaterial',
               'cylinderMaterial',
               'EnvironmentalStandards',
               'gearboxName',
               'gearboxblocks',
               'gearboxType',
               'drivingMode',
               'frontSuspensionType',
               'rearSuspensionType',
               'AssistType',
               'bodyStructure'
               ])
