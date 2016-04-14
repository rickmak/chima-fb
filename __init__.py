import skygear

@skygear.handler('chima')
def chima(request):
    if request.values.get('hub.verify_token') == 'fasengisfat':
        return request.values.get('hub.challenge')
    else:
        return 'You are not facebook'
