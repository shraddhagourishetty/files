path = 'days.txt'
days_file = open(path, 'r')
days = days_file.read()


new_path = 'naw_days.txt'
new_days = open(new_path, 'w')

title = 'days of the week\n'
new_days.write(title)
print(title)

new_days.write(days)
print(days)

days_file.close()
new_days.close()

