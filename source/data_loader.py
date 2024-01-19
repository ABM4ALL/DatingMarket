from Melodie import DataLoader

from source import data_info


class CovidDataLoader(DataLoader):
    def setup(self):
        self.load_dataframe(data_info.simulator_scenarios)
        self.load_dataframe(data_info.id_health_state)
        self.load_dataframe(data_info.id_age_group)
        self.load_dataframe(data_info.transition_prob)
