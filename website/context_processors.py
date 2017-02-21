from website import __version__


def version(request):
    return {'project_version': __version__}
