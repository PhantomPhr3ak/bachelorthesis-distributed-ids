import csv
import time
import logging
import logging.handlers

#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger().addHandler(logging.StreamHandler())

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
        print("Lade Szenario")

        # Konfiguration des Testbeds aus XML lesen
        for i in [0, 1]:
            self.configs.append(load_rtu("replay_csv/data/new_rtu_{}.xml".format(i)))

        #CSV Dateien laden
        for i in [0, 1]:
            with open("replay_csv/data/scenario_{}_subgrid_{}.csv".format(x, i), "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                self.scenario.append([])

                # skip header row
                csv_reader.__next__()

                # Daten Zeile für Zeile auslesen
                #for j in range(self.scenario_length):
                for row in csv_reader:
                    self.scenario[i].append(row)
                #try:
                #    while 1:
                #        self.scenario[i].append(csv_reader.__next__())
                #except StopIteration:
                #    pass

        # Cache erstellen
        #for i in [0, 1]:
        #    self.caches.append(create_cache(self.configs[i]))

        # Datablock erstellen
        for i in [0, 1]:
            self.datablocks.append(create_datablock(self.configs[i]))

        # Modbus Server erstellen
        for i in [0, 1]:
            self.server.append(create_server(self.configs[i], self.datablocks[i]))

        print("Server erstellt")


    def run_scenario(self):
        print("Szenario wird gestartet")

        # Modbus Server starten
        for i in [0, 1]:
            self.server[i].start()
            self.server[i].run()
            print("Started server {}".format(i))

        #debug prints
        for a in range(3):
            print("-----------------------------")
        print('configs [%s]' % ', '.join(map(str, self.configs)))
        for a in range(3):
            print("-----------------------------")
        logging.info('datablocks [%s]' % ', '.join(map(str, self.datablocks)))
        for a in range(3):
            print("-----------------------------")

        # Modbus Server (synchron) im 2 Sekundentakt mit Daten aus CSV Datei aktualisieren
        y = 0
        while y < len(self.scenario[0]):
            print("Refreshing datasets")
            # update values
            for i in [0, 1]:
                index_register = 0
                for value in self.scenario[i][y]:
                    print("value is {}".format(value))
                    # set register
                    self.datablocks[i].set(
                        self.configs[i]['registers'][index_register][0],
                        self.configs[i]['registers'][index_register][1],
                        value,
                        self.configs[i]['registers'][index_register][2],
                    )
                    index_register += 1

            # wait 2 seconds
            time.sleep(2)

            # increase number
            y += 1

        time.sleep(5)

        print("No more data available, stopping server")

        # Server wieder anhalten
        for i in [0, 1]:
            self.server[i].stop()

        print("Servers stopped")

if __name__ == '__main__':
    replay = Replay()
    replay.load_scenario(1)
    replay.run_scenario()
