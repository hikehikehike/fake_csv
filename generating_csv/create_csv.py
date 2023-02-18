import csv
import uuid

from generating_csv.models import CSVData
from faker import Faker


def generate_fake_data(columns):
    fake = Faker()
    fake_dict = {}

    for column in columns:
        type_faker_dic = {
            "Full_name": f"{fake.first_name()} {fake.last_name()}",
            "Job": fake.job(),
            "Email": fake.email(),
            "Phone_number": fake.phone_number(),
            "Address": fake.address(),
            "Integer": fake.random_int(column.start_num, column.end_num),  # TODO: add start value & end value
        }
        fake_dict[column.name] = type_faker_dic[column.type]

    return fake_dict


def create_csv(rows, schema):
    file_name = f"{schema.title}-{uuid.uuid4()}.csv"

    columns = schema.columns.all()
    field_names = [column.name for column in columns]
    separator = schema.separator
    string_character = schema.string_character

    with open(f"media/{file_name}", "w", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=field_names,
            delimiter=separator,
            quotechar=string_character,
        )
        writer.writeheader()

        for _ in range(int(rows)):
            fake_dict = generate_fake_data(columns)
            writer.writerow(fake_dict)

    csv_data = CSVData.objects.create(schema=schema, rows=rows)
    csv_data.csv_file.name = file_name
    csv_data.save()

    return csv_data
