from users.models import Person, Group, Employee
from rest_framework import viewsets
from users.serializers import PersonSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = PersonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_guest:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data='You can only delete a guest', status=status.HTTP_403_FORBIDDEN)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer

# Homepage
def index(request):
    template = loader.get_template('users/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

# Confirm sending the welcome email
@staff_member_required
def send_email(request, id):
    employee = get_object_or_404(Employee, pk=id)

    if request.method == 'POST':
        # What button has been clicked
        send_to = request.POST.get("send_to", "me")

        try:
            do_send_email(employee, send_to, request)
            messages.add_message(request, messages.SUCCESS, "The welcome email has successfully been send!")
        except Exception as e:
            messages.add_message(request, messages.ERROR, "The email hasn't been send, contact your administrator.")
        finally:
            # Redirect to employee list view
            return HttpResponseRedirect(reverse("admin:users_employee_changelist"))
    template = loader.get_template('admin/send_email.html')
    context = RequestContext(request, {"employee": employee, "current_user": request.user })
    return HttpResponse(template.render(context))

# Actually send the email
def do_send_email(employee, send_to, request):

    template = loader.get_template('admin/welcome_email.html')
    context = Context({"employee": employee})

    subject       = 'Please welcome %s %s on board!' % (employee.first_name, employee.last_name)
    email_from    = 'Post Office Square Reception <reception@1postofficesquare.co.nz>'
    plain_message = subject
    html_message  = template.render(context)
    email_to = [request.user.email]

    if send_to == 'all':
        employees = Employee.objects.filter(active=True)
        for emp in employees:
            # @todo: remove those two lines when the email template is validated
            messages.add_message(request, messages.WARNING, "Dude, did you really think I was going to send an email to all agency? The template is not even finished! Ask Arthur to unlock this functionality when the email template is ready.")
            raise NotImplementedError('Wait for the template to be validated')
            email_to.append(emp.email)

    return send_mail(subject, plain_message, email_from, email_to, fail_silently=False, html_message=html_message)
