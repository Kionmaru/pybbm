from django.utils import translation
import defaults

class PybbMiddleware(object):
    def process_request(self, request):
        request.pybb_title = defaults.PYBB_DEFAULT_TITLE
        request.pybb_avatar_dimensions = '%sx%s' % (defaults.PYBB_AVATAR_WIDTH, defaults.PYBB_AVATAR_WIDTH)
        request.pybb_default_avatar = defaults.PYBB_DEFAULT_AVATAR_URL
        if request.user.is_authenticated():
            profile = request.user.get_profile()
            language = translation.get_language_from_request(request)

            if not profile.language:
                profile.language = language
                profile.save()

            if profile.language and profile.language != language:
                request.session['django_language'] = profile.language
                translation.activate(profile.language)
                request.LANGUAGE_CODE = translation.get_language()
