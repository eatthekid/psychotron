from tests_app.models import Test

EPI = Test.create(testName='EPI', description='Тест темперамента Айзенка', url='tests/EPI/')
EPI.save()

all_tests = Test.objects.all()
print(all_tests)