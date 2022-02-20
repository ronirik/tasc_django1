from rest_framework import serializers

from applications.review.models import Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('product', 'rating')   


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['category'] = CategorySerializer(Review.objects.get(product=instance.id)).data
        return representation