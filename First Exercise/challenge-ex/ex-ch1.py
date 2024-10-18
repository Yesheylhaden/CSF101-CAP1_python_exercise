with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()

length = len(data)
print(f'the length of the data is {length}')

all_dict_data = []
sold_fruit_counts = {}
total_sum = 0
total_transactions = 0
for line in data:
    line_dictionary_temp = {
        'name': 'test',
        'action': 'test',
        'quantity': 'test',
        'item': '0',
        'price': '0'
    }

    cleaned_line = line.replace('\n', '')
    splitted_line = cleaned_line.split(',')
    line_dictionary_temp['name'] = splitted_line[0]
    line_dictionary_temp['action'] = splitted_line[1]
    line_dictionary_temp['quantity'] = int(splitted_line[2])
    line_dictionary_temp['item'] = splitted_line[3]
    line_dictionary_temp['price'] = float(splitted_line[4])
    all_dict_data.append(line_dictionary_temp)

    quantity = int(splitted_line[2])
    price = float(splitted_line[4])

    total_sum += quantity * price
    total_transactions += 1


    if splitted_line[1] == "sold":
        if splitted_line[3]  in sold_fruit_counts:
            sold_fruit_counts[splitted_line[3] ] += int(splitted_line[2])  
        else:
            sold_fruit_counts[splitted_line[3] ] = int(splitted_line[2])  

most_sold_fruit = max(sold_fruit_counts, key=sold_fruit_counts.get)
most_sold_quantity = sold_fruit_counts[most_sold_fruit]

total_sales = 0
for item in all_dict_data:
     price = float(splitted_line[4])

     total_sales += price
total_sales += round(total_sales, 2)
     

total_sold_value = 0
for item in all_dict_data:
        if item['action'] == "sold":
             sale = item['price']
             total_sold_value += sale

print(f'The total sales is: ${total_sales}')
print(f'The total value of "sold" fruits is ${total_sold_value}')
print(f'The fruit with the most transaction is: {most_sold_fruit} with {most_sold_quantity} transactions.')

average_value = total_sum / total_transactions
average_value = round(average_value, 2)
print(f'The averege value of (quantity * price) is: ${average_value}')

person_spending = {}
for line in data:
    cleaned_line = line.strip()
    splitted_line = cleaned_line.split(',')

    name = splitted_line[0]
    action = splitted_line[1]
    quantity = int(splitted_line[2])
    price = float(splitted_line[4])

    if action == "bought":
         total_spent = quantity * price

         if name in person_spending:
              person_spending[name] += total_spent
         else:
              person_spending[name] = total_spent

most_spent_person = max(person_spending, key=person_spending.get)
most_spent_amount = round(person_spending[most_spent_person], 2)

print(f'Biggest spender is: {most_spent_person} with a spending amount of ${most_spent_amount}')

with open('transaction_summary.txt', 'w') as file:
    file.write("Transaction Summary\n")
    file.write("====================\n")
    file.write(f"Total Sales: ${total_sales}\n")
    file.write(f"Most Popular Fruit: {most_sold_fruit} (Total Quantity: {most_sold_quantity})\n")
    file.write(f"Average Transaction Value: ${average_value}\n")
    file.write(f"Biggest Spender: {most_spent_person} (Total Spent: ${most_spent_amount})\n")