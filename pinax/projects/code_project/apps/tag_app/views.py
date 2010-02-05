from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from tagging.models import Tag, TaggedItem
from wiki.models import Article as WikiArticle

from pinax.apps.blog.models import Post
from pinax.apps.photos.models import Image
from pinax.apps.projects.models import Project, Task
from pinax.apps.projects.models import Topic as ProjectTopic
from pinax.apps.tribes.models import Tribe
from pinax.apps.tribes.models import Topic as TribeTopic



def tags(request, tag, template_name="tags/index.html"):
    tag = get_object_or_404(Tag, name=tag)
    
    alltags = TaggedItem.objects.get_by_model(Post, tag).filter(status=2)
    
    phototags = TaggedItem.objects.get_by_model(Image, tag)
    
    project_tags = TaggedItem.objects.get_by_model(Project, tag).filter(deleted=False)
    project_topic_tags = TaggedItem.objects.get_by_model(ProjectTopic, tag).filter(project__deleted=False)
    project_task_tags = TaggedItem.objects.get_by_model(Task, tag).filter(project__deleted=False)
    
    tribe_tags = TaggedItem.objects.get_by_model(Tribe, tag).filter(deleted=False)
    tribe_topic_tags = TaggedItem.objects.get_by_model(TribeTopic, tag).filter(tribe__deleted=False)
    
    # @@@ TODO: tribe_wiki_article_tags and project_wiki_article_tags
    wiki_article_tags = TaggedItem.objects.get_by_model(WikiArticle, tag)
    
    return render_to_response(template_name, {
        "tag": tag,
        "alltags": alltags,
        "phototags": phototags,
        "project_tags": project_tags,
        "project_topic_tags": project_topic_tags,
        "project_task_tags": project_task_tags,
        "tribe_tags": tribe_tags,
        "tribe_topic_tags": tribe_topic_tags,
        "wiki_article_tags": wiki_article_tags,
    }, context_instance=RequestContext(request))
