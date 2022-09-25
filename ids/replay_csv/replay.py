import csv
import time
import pprint
import logging
import logging.handlers

# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler())

from mosaikrtu.rtu_model import create_server, create_cache, create_datablock, load_rtu


# TODO: translate comments into english

class Replay:

    def __init__(self):
        self.server = []
        self.datablocks = []
        self.configs = []
        # self.caches = []
        self.scenario_length = 21
        self.scenario = []
        self.amnt_switches = [1, 2]  # TODO: set automatically depending on config
        self.amnt_sensors = [12, 13]  # TODO: set automatically depending on config

    def load_scenario(self, x):
        print("Load configs and scenarios form file")

        # Load config of RTUs from xml files
        for i in [0, 1]:
            self.configs.append(load_rtu("replay_csv/data/new_rtu_{}.xml".format(i)))

        # Read CSV data
        for i in [0, 1]:
            with open("replay_csv/data/scenario_{}_subgrid_{}.csv".format(x, i), "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";")
                self.scenario.append([])

                # skip header row
                csv_reader.__next__()

                # Load Data row by row and save it
                for row in csv_reader:
                    self.scenario[i].append(row)

        # Create Datablocks
        for i in [0, 1]:
            self.datablocks.append(create_datablock(self.configs[i]))

        # Create Modbus servers
        for i in [0, 1]:
            self.server.append(create_server(self.configs[i], self.datablocks[i]))

        print("Server erstellt")

    def run_scenario(self):
        print("Szenario is beeing started")

        # Starting Modbus servers
        for i in [0, 1]:
            self.server[i].start()
            # self.server[i].run()
            print("Started server {}".format(i))

        # debug prints
        # for a in range(3):
        #    print("----------------------------- \n")
        # print('configs [%s]' % ', '.join(map(str, self.configs)))
        # for a in range(3):
        #    print("----------------------------- \n")
        # print('scenario [%s]' % ', '.join(map(str, self.scenario)))
        # for a in range(3):
        #    print("----------------------------- \n")

        # load new dataset every two seconds into both Modbus Servers (synchronous)
        y = 0
        while y < len(self.scenario[0]):
            print("Refreshing datasets")
            # update values
            for i in [0, 1]:
                index_register = 0
                for value in self.scenario[i][y]:
                    if value != "":

                        config_item = list(self.configs[i]['registers'].values())[index_register]

                        if config_item[2] == "64bit_float":
                            value = float(value)

                        print("value is {}     config is {}\n".format(value, config_item))

                        # set register
                        self.datablocks[i].set(
                            config_item[0],
                            config_item[1],
                            value,
                            config_item[2],
                        )
                        index_register += 1

            # wait 2 seconds
            time.sleep(2)

            # increase "time" aka csv row index
            y += 1

        time.sleep(5)

        print("No more data available, stopping server")

        # Server wieder anhalten
        for i in [0, 1]:
            self.server[i].stop()

        print("Servers stopped")


if __name__ == '__main__':
    for i in [1, 2, 3, 4]:
        print("starting scenario {}".format(i))
        replay = Replay()
        replay.load_scenario(i)
        replay.run_scenario()
        print("finished scenario {}".format(i))
        time.sleep(10)
