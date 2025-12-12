from allauth.account.signals import user_logged_in, user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def signal_user_signed_up(request, user, sociallogin=None, **kwargs):
    print(request)
    print(user)
    print(sociallogin)



@receiver(user_logged_in)
def signal_user_logged_in(request, user, sociallogin=None, **kwargs):
    print("Request:", request)
    print("User:", user)
    print("Sociallogin:", sociallogin)