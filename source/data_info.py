import sqlalchemy

from Melodie import DataFrameInfo


simulator_scenarios = DataFrameInfo(
    df_name="simulator_scenarios",
    file_name="SimulatorScenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "run_num": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "initial_infected_percentage": sqlalchemy.Float(),
        "young_percentage": sqlalchemy.Float(),
        "infection_prob": sqlalchemy.Float(),
    },
)

id_health_state = DataFrameInfo(
    df_name="ID_HealthState",
    file_name="ID_HealthState.xlsx",
    columns={
        "id_health_state": sqlalchemy.Integer(),
        "name": sqlalchemy.String()
    },
)

id_age_group = DataFrameInfo(
    df_name="ID_AgeGroup",
    file_name="ID_AgeGroup.xlsx",
    columns={
        "id_age_group": sqlalchemy.Integer(),
        "name": sqlalchemy.String(),
    },
)

transition_prob = DataFrameInfo(
    df_name="Data_TransitionProb",
    file_name="Data_TransitionProb.xlsx",
    columns={
        "id_age_group": sqlalchemy.Integer(),
        "id_health_state": sqlalchemy.Float(),
        "unit": sqlalchemy.String(),
        "infected": sqlalchemy.Float(),
        "recovered": sqlalchemy.Float(),
        "dead": sqlalchemy.Float(),
    },
)
