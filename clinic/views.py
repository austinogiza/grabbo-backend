from rest_framework.views import APIView
from clinic.models import Blog, Career, Comments, Contact, Departments, Professional
from clinic.serializers import BlogListSerializer, CareerListSerializer, CommentSerializer, ContactSerializer, DepartmentListSerializer, ProfessionaListSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.


class BlogListView(ListAPIView):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all().order_by('-date')
    permission_classes = (AllowAny, )


class DepartmentListView(ListAPIView):
    serializer_class = DepartmentListSerializer
    queryset = Departments.objects.all().order_by('date')
    permission_classes = (AllowAny, )


class DepartmentDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Departments.objects.all()
    serializer_class = DepartmentListSerializer

class PersonnelListView(ListAPIView):
    serializer_class = ProfessionaListSerializer
    permission_classes = (AllowAny, )
    # queryset = Professional.objects.all().order_by('-date')

    def get_queryset(self):
        return Professional.objects.order_by('date')

class PersonnelDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Professional.objects.all()
    serializer_class = ProfessionaListSerializer


class BlogDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer




class BlogCommentView(APIView):
    permission_classes = (AllowAny,)
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    def post(self, request, *args,**kwargs):
        slug= request.data.get('slug')
        user = request.data.get("name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        comment = request.data.get("comment")

        post = get_object_or_404(Blog, slug=slug)
        comment_post = Comments(
            user=user,
            comment=comment,
            post = post

        )
        comment_post.save()
        post.comments.add(comment_post)
        post.save()

        subject = post.title
        context ={
            "name": user,
            "email": email,
            "phone":phone,
            "message": comment
        }
        template = render_to_string('ivf.html', context)
        mail = EmailMessage(
             'We have a new comment',
             template,
               "contact@grabbofertilityclinic.com",
            ['contact@grabbofertilityclinic.com']
        )
        mail.fail_silently = False
        mail.send()
        return Response(status=HTTP_200_OK)


class BlogCommentFetchView(APIView):
    permission_classes = (AllowAny,)
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    def get(self, request, *args,**kwargs):
        slug = request.query_params.get('slug')
        comments = Comments.objects.filter(post__slug=slug)
        serializer = CommentSerializer(comments, many=True).data
        return Response(serializer,status=HTTP_200_OK)


class HomePersonnelListView(ListAPIView):
    serializer_class = ProfessionaListSerializer
    queryset = Professional.objects.all().order_by("-date")[:6]
    permission_classes = (AllowAny, )

class HomeDepartmentListView(ListAPIView):
    serializer_class = DepartmentListSerializer
    queryset = Departments.objects.all().order_by('date')[:4]
    permission_classes = (AllowAny, )

class CareerListView(ListAPIView):
    serializer_class = CareerListSerializer
    queryset = Career.objects.all()
    permission_classes = (AllowAny, )

class CareerDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)
    queryset = Career.objects.all()
    serializer_class = CareerListSerializer


class ContactView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')
        contact = Contact(
            name=name,
email=email,
subject=subject,
message=message,
        )
        contact.save()


        context ={
            "name": name,
            "email": email,
            "subject": subject,
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
