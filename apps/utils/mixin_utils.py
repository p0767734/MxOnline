#_*_coding:utf-8 _*_

_author_ = 'bobby'
_date_ = '2017/11/20 21:07'


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request,*args,**kwargs)