from Exam_Prep_2.profiles.models import Profile


def has_profile(request):
    return {
        'has_profile': Profile.objects.exists()
    }
