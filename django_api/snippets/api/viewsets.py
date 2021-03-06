from snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# class SnippetViewSet(viewsets.ViewSet):
#
#     def list(self,request):
#         queryset =Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)

class SnippetViewSet(viewsets.ModelViewSet):
    # list, create, retrieve, update, partial_update, destroy

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)