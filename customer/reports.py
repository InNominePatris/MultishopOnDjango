from reports.base import ModelReport
from .models import Customer


class CustomerReport(ModelReport):
    name = "Report"
    queryset = Customer.objects.all()


report = CustomerReport()

report.collect_data()

report.generate_output()

