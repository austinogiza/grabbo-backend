from rest_framework.views import APIView
from .models import  Contact
from .serializers import ContactSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.






class ContactView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        message = request.data.get('message')
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
        contact.save()
        context ={
            "name": name,
            "email": email,
            "phone": phone,
            "message": message
        }
        template = render_to_string('email.html', context)
        email = EmailMessage(
             'We have a new Contact mail',
             template,
               "contact@grabbofertilityclinic.com",
            ['contact@grabbofertilityclinic.com']
        )
        email.fail_silently = False
        email.send()
        return Response(status=HTTP_201_CREATED)
