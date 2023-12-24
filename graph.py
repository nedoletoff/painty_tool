import datetime
import numpy as np
import matplotlib.pyplot as plt
import timestamp
from evtx import PyEvtxParser
import json
import pytz


def load_events(path, event_ids):
    events = []
    parser = PyEvtxParser(path)

    for record in parser.records_json():
        data = json.loads(record['data'])
        event_id = int(data["Event"]["System"]["EventID"])

        if event_id in event_ids:
            timestamp = record["timestamp"][:19]
            event_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc).astimezone(
                tz=None)
            events.append((event_id, event_time))

    return events


def draw_stacked_histogram(x_values, y_values, x_label='', y_label='', subplot_num=0, x_limit=-1, y_limit=-1,
                           legend_labels=None, linewidth=0.2, colors=None):
    if subplot_num != 0:
        plt.subplot(subplot_num)

    if x_limit > 0:
        plt.xlim(0, x_limit)

    if y_limit > 0:
        plt.ylim(0, y_limit)

    bottom = np.zeros(y_values.shape[1])

    for y, color in zip(y_values, colors):
        plt.bar(x_values, y, bottom=bottom, width=1, linewidth=linewidth, edgecolor="white", color=color)
        bottom += y

    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.grid(visible=True)
    if legend_labels is not None:
        plt.legend(legend_labels)


def draw_event_history(events, figure_num=1):
    unique_ids = np.unique([event_id for event_id, _ in events])
    groups = np.zeros((unique_ids.size, 24))

    for event_id, event_time in events:
        i = np.where(unique_ids == event_id)[0][0]
        groups[i][event_time.hour] += 1

    color_palette = ['#1b2634', '#203f5f', '#ffcb00', '#fde5b2', '#ff4967', '#ba6ae0']
    colors = [color_palette[i] for i in np.argsort(np.sum(groups, axis=1))]

    plt.figure(figure_num)
    draw_stacked_histogram(np.arange(24), groups, legend_labels=unique_ids, colors=colors)


def separate_events_by_days(events, delta):
    separated_events = []
    temp_events = []
    current_event_time = events[0][1]

    for event in events:
        if event[1] - current_event_time > delta:
            separated_events.append(temp_events)
            temp_events = []
            current_event_time = event[1]
        temp_events.append(event)

    if temp_events:
        separated_events.append(temp_events)

    return separated_events


def process_data(event_filter, save=True):
    event_journals = {
        "V13": "journals/V13/tttt.evtx",
        "V3": "journals/V3/fdgh.evtx",
        "V1": "journals/V1/Art_logs.evtx",
        "V3_1": "journals/V3/nero4.evtx"
    }
    event_days = {
        "V13": 3,
        "V3": 3,
        "V1": 30,
        "V3_1": 5}

    for version, journal_path in event_journals.items():
        events = load_events(journal_path, event_filter)
        separated_events = separate_events_by_days(events, datetime.timedelta(days=event_days[version]))

        for i, event_group in enumerate(separated_events):
            draw_event_history(event_group, (i + 1) * 1000 + version)
            if save:
                plt.savefig(f"Dataset/{version}/{version}/img_{i}.png")


def visualize_security_events(path, event_filter, delta):
    events = load_events(path, event_filter)
    daily_events = separate_events_by_days(events, datetime.timedelta(days=delta))

    for i, daily_event in enumerate(daily_events):
        draw_event_history(daily_event, i)
    plt.show()


if __name__ == "__main__":
    event_filter = np.array([4616, 4624, 4634, 4672, 5058, 5061])
    visualize_security_events("jjj.evtx", event_filter, 500)
