from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def analysis(request):
    return render_to_response("analysis.html",
                              locals(),
                              context_instance=RequestContext(request))