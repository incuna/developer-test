import json

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


def course_list(request):
    # simulate loading the data
    fileDescriptor = open(settings.ROOT_DIR+'/data/course_list.json')
    courses = json.load(fileDescriptor)
    fileDescriptor.close()

    context = RequestContext(request, {
        'courses': courses
    })
    return render_to_response('course_list.html', context)
