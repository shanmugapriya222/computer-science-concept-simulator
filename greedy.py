def activity_selection(activities):
    """
    Greedy Activity Selection Algorithm.

    Each activity is:
    (activity_name, start_time, finish_time)

    Strategy:
    Always select the activity that finishes earliest.
    """

    # Sort activities by finish time
    sorted_activities = sorted(
        activities,
        key=lambda activity: activity[2]
    )

    selected = []
    steps = []

    last_finish_time = -1

    for activity in sorted_activities:

        name, start, finish = activity

        if start >= last_finish_time:

            selected.append(activity)

            steps.append(
                f"Selected {name}: "
                f"starts at {start}, finishes at {finish}"
            )

            last_finish_time = finish

        else:

            steps.append(
                f"Rejected {name}: "
                f"starts at {start}, "
                f"because it overlaps with the selected activity."
            )

    return selected, steps