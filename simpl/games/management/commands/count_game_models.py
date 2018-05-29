import djclick as click

from ... import models


@click.command()
@click.option('--slug', '-s', type=str, help='Game slug.')
def command(slug):
    """Print count of game's model objects."""

    phase_count = models.Phase.objects.filter(game__slug=slug).count()
    role_count = models.Role.objects.filter(game__slug=slug).count()
    run_count = models.Run.objects.filter(game__slug=slug).count()

    runuser_count = models.RunUser.objects.filter(run__game__slug=slug).count()
    world_count = models.World.objects.filter(run__game__slug=slug).count()

    runuser_scenario_count = models.Scenario.objects.filter(runuser__run__game__slug=slug).count()
    world_scenario_count = models.Scenario.objects.filter(world__run__game__slug=slug).count()
    scenario_count = runuser_scenario_count + world_scenario_count

    runuser_period_count = models.Period.objects.filter(scenario__runuser__run__game__slug=slug).count()
    world_period_count = models.Period.objects.filter(scenario__world__run__game__slug=slug).count()
    period_count = runuser_period_count + world_period_count

    runuser_decision_count = models.Decision.objects.filter(period__scenario__runuser__run__game__slug=slug).count()
    world_decision_count = models.Decision.objects.filter(period__scenario__world__run__game__slug=slug).count()
    decision_count = runuser_decision_count + world_decision_count

    runuser_result_count = models.Result.objects.filter(period__scenario__runuser__run__game__slug=slug).count()
    world_result_count = models.Result.objects.filter(period__scenario__world__run__game__slug=slug).count()
    result_count = runuser_result_count + world_result_count

    click.echo("Phase count: {0}".format(phase_count))
    click.echo("Role count: {0}".format(role_count))
    click.echo("Run count: {0}".format(run_count))
    click.echo("RunUser count: {0}".format(runuser_count))
    click.echo("World count: {0}".format(world_count))
    click.echo("Scenario count: {0}".format(scenario_count))
    click.echo("Period count: {0}".format(period_count))
    click.echo("Decision count: {0}".format(decision_count))
    click.echo("Result count: {0}".format(result_count))

