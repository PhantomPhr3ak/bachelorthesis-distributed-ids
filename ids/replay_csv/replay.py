import csv

from ids.deployment.testbed.mosaikrtu.dvcd.data import DataBlock
from ids.deployment.testbed.mosaikrtu.dvcd.server import Server
from ids.deployment.testbed.mosaikrtu.rtu_model import create_server, create_cache, create_datablock, load_rtu


class Replay:

    def __init__(self):
        self.server = []
        self.datablock = []
        self.conf = []
        self.cache = []
        self.scenario_length = 21
        self.scenario = []

    def replayScenario(self, x):
        # Konfiguration des Testbeds aus XML lesen
        for i in [0, 1]:
            self.conf[i] = load_rtu("../deployment/testbed/data/config_files/new_rtu_{}.xml".format(i))

        # Cache erstellen
        for i in [0, 1]:
            self.cache[i] = create_cache(self.conf[i])

        # Datablock erstellen
        for i in [0, 1]:
            self.datablock[i] = create_datablock(self.conf[i])

        # Modbus Server erstellen
        for i in [0, 1]:
            self.server[i] = create_server(self.conf[i], self.datablock[i])
            self.server[i].run()

        # Modbus Server (synchron) im Sekundentakt mit Daten aus CSV Datei aktualisieren
        for i in [0, 1]:
            with open("data/scenario_{}_subgrid_{}.csv".format(x, i), "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                self.scenario[i] = []
                for j in range(self.scenario_length):
                    self.scenario[i].append()



if __name__ == '__main__':
    replayScenario()
