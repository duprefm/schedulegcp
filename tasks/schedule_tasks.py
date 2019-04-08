"""Change a state for all matching instances in a project."""
import logging

from gcp.compute import Compute
from gcp.sql import Sql
from gcp.instances_group import Instancegroup


def change_state(tagkey, tagvalue, action, project):
    """
    Change a state for all matching instances in a project.
    Args:
        tagkey: tag key
        tagvalue: tag value
        action: stop 0 start 1
        project: project id

    Returns:

    """

    compute = Compute(project)
    sql = Sql(project)
    instance_group = Instancegroup(project)
    logging.debug("change_state %s action %s", project, action)
    compute.change_status(action, tagkey, tagvalue)
    sql.change_status(action, tagkey, tagvalue)
    instance_group.change_status(action, tagkey, tagvalue)
    return 'ok', 200
