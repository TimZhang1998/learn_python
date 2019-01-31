from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import TopicForm, EntryForm

from .models import Topic, Entry


def index(request):
    """index"""

    return render(request, '../templates/learning_logs/index.html')


@login_required
def topics(request):
    """topics"""

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, '../templates/learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """a certain topic"""

    topic = get_object_or_404(Topic, id=topic_id)

    # ensure that the user match with its owner correctly
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, '../templates/learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """add a new topic"""

    if request.method != 'POST':
        # if not post a form, create a new form
        form = TopicForm()
    else:
        # if post a form, handle the data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, '../templates/learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """add a new entry"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # if not post a form, create a new form
        form = EntryForm()
    else:
        # if post a form, handle the data
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                kwargs={"topic_id": topic.id}))
    context = {'topic': topic, 'form': form}
    return render(request, '../templates/learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """edit a certain entry"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # ensure that the user match with its owner correctly
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # initial request, fill the form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                kwargs={"topic_id": topic.id}))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, '../templates/learning_logs/edit_entry.html', context)
