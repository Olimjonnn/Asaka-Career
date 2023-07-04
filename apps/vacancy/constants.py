class JOB_TYPE:
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    INTERNSHIP = 'internship'
    CONTRACT = 'contract'
    TEMPORARY = 'temporary'

    CHOICES = (
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (INTERNSHIP, 'Internship'),
        (CONTRACT, 'Contract'),
        (TEMPORARY, 'Temporary')
    )


class CANDIDATE_LEVEL:
    JUNIOR = 'junior'
    MIDDLE = 'middle'
    SENIOR = 'senior'
    TEAM_LEAD = 'team_lead'

    CHOICES = (
        (JUNIOR, 'Junior'),
        (MIDDLE, 'Middle'),
        (SENIOR, 'Senior'),
        (TEAM_LEAD, 'Team Lead')
    )
