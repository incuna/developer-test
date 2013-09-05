import json

from django.conf import settings
from django.shortcuts import render_to_response


def course_list(request):
    # simulate loading the data
    f = open(settings.ROOT_DIR+'/data/course_list.json')
    courses = json.load(f)
    f.close()

    return render_to_response('course_list.html', {'courses': courses})
