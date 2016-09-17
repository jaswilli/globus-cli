import click

from globus_cli.safeio import safeprint
from globus_cli.parsing import common_options, task_id_option
from globus_cli.helpers import outformat_is_json, print_json_response

from globus_cli.services.transfer.helpers import get_client


@click.command('cancel', short_help='Cancel a Task',
               help='Cancel a Task owned by the current user')
@common_options
@task_id_option(helptext='ID of the Task which you want to cancel')
def cancel_task(task_id):
    """
    Executor for `globus transfer task cancel`
    """
    client = get_client()

    res = client.cancel_task(task_id)

    if outformat_is_json():
        print_json_response(res)
    else:
        safeprint(res['message'])
