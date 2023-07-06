def study_schedule(permanence_period, target_time):
    count = 0
    if not target_time:
        return None
    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time and target_time <= end:
            count += 1
    return count
