from pathlib import Path

from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, DbtProject, dbt_assets

dbt_project = DbtProject(
    project_dir=Path(__file__).parent.parent / "dbt_project",
    profiles_dir=Path(__file__).parent.parent,
)
dbt_project.prepare_if_dev()


@dbt_assets(manifest=dbt_project.manifest_path, select="tag:2023")
def dbt_2023_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


@dbt_assets(manifest=dbt_project.manifest_path, select="tag:2019")
def dbt_2019_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
