from rest_framework import generics


from applications.review.selializers import ReviewSerializer

from applications.review.models import Review


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer