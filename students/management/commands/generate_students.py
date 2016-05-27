from students.models import Student
import requests, json, random
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        randusersreq = requests.get("https://randomuser.me/api/?results=100&nat=NL")
        randusersjson = json.loads(randusersreq.text)
        randusers= randusersjson['results']
        randusernames = map(lambda x: x["name"]["first"].capitalize() + " " + x["name"]["last"].capitalize(), randusers)
        for user in randusernames:
            st = Student(name=user,
                     AK_points=random.randint(0,20), IT_points=random.randint(0,20), KU_points=random.randint(0,20), NL_points=random.randint(0,20),
                     RE_points=random.randint(0,20), EN_points=random.randint(0,20), GE_points=random.randint(0,20), MA_points=random.randint(0,20))
            st.save()

