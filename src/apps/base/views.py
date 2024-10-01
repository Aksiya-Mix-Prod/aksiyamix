from rest_framework import generics, views


class CustomAPIView(views.APIView):
    pass


class CustomGenericAPIView(generics.GenericAPIView):
    pass


class CustomListAPIView(generics.ListAPIView):
    pass


class CustomCreateAPIView(generics.CreateAPIView):
    pass


class CustomRetrieveAPIView(generics.RetrieveAPIView):
    pass


class CustomUpdateAPIView(generics.UpdateAPIView):
    pass


class CustomDestroyAPIView(generics.DestroyAPIView):
    pass


class CustomListCreateAPIView(generics.ListCreateAPIView):
    pass


class CustomRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    pass


class CustomRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    pass


class CustomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    pass