import csv
import time

from mosaikrtu.rtu_model import create_server, create_cache, create_datablock, load_rtu

#TODO: translate comments into english

class Replay:

    def __init__(self):
        self.server = []
        self.datablocks = []
        self.configs = []
        self.caches = []
        self.scenario_length = 21
        self.scenario = []
        self.amnt_switches = [1, 2]         #TODO: set automatically depending on config
        self.amnt_sensors = [12, 13]        #TODO: set automatically depending on config

    def load_scenario(self, x):
        # Konfiguration des Testbeds aus XML lesen
        for i in [0, 1]:
            self.configs[i] = load_rtu("data/new_rtu_{}.xml".format(i))

        #CSV Dateien laden
        for i in [0, 1]:
            with open("data/scenario_{}_subgrid_{}.csv".format(x, i), "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                self.scenario[i] = []

                # skip header row
                csv_reader.__next__()

                # Daten Zeile für Zeile auslesen
                for j in range(self.scenario_length):
                    self.scenario[i].append(csv_reader.__next__())

        # Cache erstellen
        for i in [0, 1]:
            self.caches[i] = create_cache(self.configs[i])

        # Datablock erstellen
        for i in [0, 1]:
            self.datablocks[i] = create_datablock(self.configs[i])

        # Modbus Server erstellen
        for i in [0, 1]:
            self.server[i] = create_server(self.configs[i], self.datablocks[i])


    def run_scenario(self):
        # Modbus Server starten
        for i in [0, 1]:
            self.server[i].run()

        # Modbus Server (synchron) im 2 Sekundentakt mit Daten aus CSV Datei aktualisieren
        y = 0
        while y < self.scenario_length:
            # update values
            for i in [0, 1]:
                # set coils
                self.datablocks[i].set(_type="co", address="0", _datatype="bool", values=self.scenario[i][y][:self.amnt_switches[i]])

                #set holding registers
                self.datablocks[i].set(_type="co", address="0", _datatype="64bit_float", values=self.scenario[i][y][self.amnt_switches[i]:])

            # wait 2 seconds
            time.sleep(2)

            # increase number
            y += 1

        # Server wieder anhalten
        for i in [0, 1]:
            self.server[i].stop()

if __name__ == '__main__':
    replay = Replay()
    replay.load_scenario(1)
    replay.run_scenario()
