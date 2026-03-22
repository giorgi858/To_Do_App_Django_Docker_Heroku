from allauth.account.adapter import DefaultAccountAdapter

class CeleryAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        from .tasks import send_allauth_email_task
        
        # Create a simple dictionary that ONLY contains strings and numbers
        # This is safe for Celery/Redis
        serializable_context = {
            'user_id': context['user'].pk,
            'activate_url': context.get('activate_url'),
            'key': context.get('key'),
        }
        
        # Pass the SAFE dictionary, not the original 'context'
        send_allauth_email_task.delay(serializable_context, template_prefix, email)
