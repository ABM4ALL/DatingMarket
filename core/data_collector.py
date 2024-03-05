import os

import pandas as pd
from Melodie import DataCollector


class DatingDataCollector(DataCollector):

    def setup(self):
        """
        This function is automatically called. Users can define which data to be collected and saved.
        Then, in model.run(), users can call data_collector.collect() and data_collector.save().

        In DataCollector, users can define "simple and standard structure" data, meaning that
         - micro-level agent data --> indexed by id_scenario, id_run, id_agent, period
         - macro-level environment data --> indexed by id_scenario, id_run, period
        For "complicated and customized structure" data, users can collect and save in the `environment`.
        """
        self.add_agent_property(container_name="men", property_name="income_before_shock")
        self.add_agent_property(container_name="men", property_name="income")
        self.add_agent_property(container_name="men", property_name="social")
        self.add_agent_property(container_name="men", property_name="saving")
        self.add_agent_property(container_name="women", property_name="income_before_shock")
        self.add_agent_property(container_name="women", property_name="income")
        self.add_agent_property(container_name="women", property_name="social")
        self.add_agent_property(container_name="women", property_name="saving")
        self.add_environment_property(property_name="total_assessment")
