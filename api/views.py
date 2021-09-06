from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


# Create your views here.

@api_view(['GET'])
def getData(request):
    notes = Todo.objects.filter(user=request.user)
    serializer = TodoSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewDataById(request, pk):
    notes = Todo.objects.get(id=pk)
    serializer = TodoSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createData(request):
    data = request.data
    note = Todo.objects.create(
        note=data['note'],
        user=request.user
    )
    serializer = TodoSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateData(request, pk):
    # data = request.data
    note = Todo.objects.get(id=pk)
    serializer = TodoSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request, pk):
    note = Todo.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')
