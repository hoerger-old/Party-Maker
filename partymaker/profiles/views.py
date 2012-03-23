from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

def userprofile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = user.get_profile()
        fields = user.userfield_set.extra(order_by=["position"])
        c={'theuser':user, 'theuserprofile': profile, "fields":fields}
        return render_to_response('profiles/userprofile.xhtml',c, context_instance=RequestContext(request))
    except User.DoesNotExist:
        return render_to_response('profiles/doesnotexist.xhtml',{'username': username}, context_instance=RequestContext(request))
