from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TodoSerializer, UserSerializer
from rest_framework import status, generics
from django.contrib.auth.models import User
from note.models import Todo

class NoteLIstCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_url_kwarg = 'product_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



# class UserNoteListAPIView(generics.ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
    
#     def get_queryset(self):
#         print('user', self.request.user.id)
#         qs = super().get_queryset()
#         return qs.filter(user=self.request.user.id)
    
    
    
# @api_view(['GET', 'POST'])
# def api_home_page(request):
#     if request.method == 'GET':
#         note_queryset = Note.objects.all()
#         serilizerData = NoteSerializer(note_queryset, many=True)
#         return Response(serilizerData.data)
#     if request.method == "POST":

#         data = request.data
#         serializeData = NoteSerializer(data=data)
#     if serializeData.is_valid():
#         serializeData.save()
#         return Response(serializeData.data, status=status.HTTP_201_CREATED)
#     return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT', 'DELETE'])
# def note_detail(request, pk):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'DELETE':
        
#         note.delete()
#         data = request.data
#         serializeData = NoteSerializer(note)
#         return Response(serializeData.data, status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'PUT':
#         data = request.data
#         serializeData = NoteSerializer(note, data=data)
#         if serializeData.is_valid():
#             serializeData.save()
#             return Response(serializeData.data)
#         return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)
    

