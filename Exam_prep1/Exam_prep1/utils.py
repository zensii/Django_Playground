from Exam_prep1.profiles.models import Profile


def get_usr_obj() -> Profile | None:
    """
    Returns a user object if one exists, otherwise returns None.
    """
    return Profile.objects.first()