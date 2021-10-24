import pandas as pd
import pm4py

"""
# Notes

Change "sid" column to "case_id" and "name" to "activity".
"""


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=',')
    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    return event_log


def export_csv():
    event_log = pm4py.format_dataframe(pd.read_csv('C:/Users/Christian Poulsen/Downloads/running-example.csv', sep=';'),
                                       case_id='case_id',
                                       activity_key='activity', timestamp_key='timestamp')
    event_log.to_csv('C:/Users/Christian Poulsen/Desktop/running-example-exported.csv')


def discover_inductive(log):
    process_tree = pm4py.discover_process_tree_inductive(log)
    pm4py.view_process_tree(process_tree)


def discover_heuristic(log):
    process_map = pm4py.discover_heuristics_net(log)
    pm4py.view_heuristics_net(process_map)


if __name__ == "__main__":
    log = import_csv("./tracking.csv")

    discover_inductive(log)
    discover_heuristic(log)

