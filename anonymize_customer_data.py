import sys
import csv
from faker import Faker


def create_customer_records(no_of_records):
    faker = Faker()

    with open('customers.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        for i in range(1,no_of_records):
            writer.writerow([faker.first_name(), faker.last_name(), faker.street_address(), faker.date_of_birth()])

def anonymize_customer_records():
    faker = Faker()
    
    with open('customers.csv') as source_file:
        with open('anonymized_customers.csv', 'w') as output_file:
            csv_reader = csv.reader(source_file, delimiter=',')
            writer = csv.writer(output_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    writer.writerow(row)
                    line_count += 1
                else:
                    anonymized_row = [faker.first_name(), faker.last_name(), faker.street_address(), row[3]]
                    writer.writerow(anonymized_row)
                    line_count += 1
            print(f'Processed {line_count} lines.')

if __name__ == '__main__':
    create_customer_records(int(sys.argv[1]))
    anonymize_customer_records()
                