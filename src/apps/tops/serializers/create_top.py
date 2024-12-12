import calendar

from django.utils.timezone import now

from apps.base.exceptions import CustomAPIExceptionError
from apps.base.serializers import CustomModelSerializer
from apps.tops.models import TopDiscount, TopCalendar


class CreateTopDiscountSerializer(CustomModelSerializer):
    class Meta:
        model = TopDiscount
        fields = '__all__'
        
    def create(self, validated_data):
        company_top_tariff_counts = validated_data["discount"].company.top_tariff_counts
        if int(company_top_tariff_counts) < len(validated_data["dates"]):
            raise CustomAPIExceptionError(code=400, detail="You have not enough top tariff counts")
        company_top_tariff_counts = int(company_top_tariff_counts) - len(validated_data["dates"])
        validated_data["discount"].company.top_tariff_counts = str(company_top_tariff_counts)
        validated_data["discount"].company.save()
        for date in validated_data["dates"]:
            if date < now().date():
                raise CustomAPIExceptionError(code=400, detail="Date is not valid")
            _, month_days = calendar.monthrange(date.year, date.month)
            try:
                top_calendar = TopCalendar.objects.get(
                    year=date.year,
                    month=date.month)
            except:
                days = []
                for i in range(int(month_days)):
                    days.append([False, False, False])
                top_calendar = TopCalendar.objects.create(
                    year=date.year,
                    month=date.month,
                    days=days)
                top_calendar.save()
            count = 0
            for i in top_calendar.days:
                count = count + 1
                if count == date.day:
                    a_count = 0
                    for a in i:
                        a_count = a_count + 1
                        if a == False:
                            top_calendar.days[count-1][a_count-1] = True
                            top_calendar.save()
                            break
                        if a_count == 3:
                            raise CustomAPIExceptionError(code=400, detail="This day is full")
        return super().create(validated_data)