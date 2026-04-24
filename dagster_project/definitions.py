from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import dbt_2019_assets, dbt_2023_assets, dbt_project
from .jobs import daily_2019_schedule, daily_2023_schedule, dbt_2019_job, dbt_2023_job

defs = Definitions(
    assets=[dbt_2023_assets, dbt_2019_assets],
    jobs=[dbt_2023_job, dbt_2019_job],
    schedules=[daily_2023_schedule, daily_2019_schedule],
    resources={
        "dbt": DbtCliResource(project_dir=dbt_project),
    },
)
