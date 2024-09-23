from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def home(request):
    logger.info('Home page accessed')
    return render(request, 'home.html')


def about(request):
    logger.info('About page accessed')
    return render(request, 'about.html')