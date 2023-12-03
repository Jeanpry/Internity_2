'''def filter_by_type(internships, Type_of_internship):
    return internships[internships['Type_of_internship'] == Type_of_internship]


def filter_by_location(internships, location):
    return internships[internships['location'] == location]

def filter_by_duration(internships, duration):
    return internships[internships['duration'] == duration]'''

def filter_by_type(internships, Type_of_internship):
    filtered = internships[internships['Type_of_internship'] == Type_of_internship]
    return filtered if not filtered.empty else internships

def filter_by_location(internships, location):
    filtered = internships[internships['location'] == location]
    return filtered if not filtered.empty else internships

def filter_by_duration(internships, duration):
    filtered = internships[internships['duration'] == duration]
    return filtered if not filtered.empty else internships
