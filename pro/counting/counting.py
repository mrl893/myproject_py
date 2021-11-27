def  get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.iteritems():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count
