from django.template import RequestContext
def custom_proc(request):
		return {
				'app':'code share website',
				'request':request,
				'ip_address':request.META['REMOTE_ADDR']
				}
