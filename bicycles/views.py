from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BicycleSerializer
from .models import Bicycle

class AllBikes(APIView):
    def get(self, request, pk=None):
        if pk:  
            data = Bicycle.objects.get(pk=pk)
            serializer = BicycleSerializer(data)
        else:
            data = Bicycle.objects.all()
            serializer = BicycleSerializer(data, many=True)
        return Response({"result": serializer.data})
	
    def post(self, request):
        bike = request.data
        serializer = BicycleSerializer(data=bike)
        if serializer.is_valid(raise_exception=True):
            bike_saved = serializer.save()
        return Response({"result": f"{bike_saved.make} saved"})

    def put(self, request, pk):
        saved_bike = get_object_or_404(Bicycle.objects.all(), pk=pk)
        data = request.data
        serializer = BicycleSerializer(instance=saved_bike, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_bike = serializer.save()
        return Response({"result": f"{saved_bike.make} updated"})

    def delete(self, request, pk):
        wine = get_object_or_404(Bicycle.objects.all(), pk=pk)
        wine.delete()
        return Response({"result": f"Bicylce id {pk} deleted"},status=204)
