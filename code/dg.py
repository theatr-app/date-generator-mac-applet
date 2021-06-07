from datetime import date, timedelta

print("Running script")

def parse_inputline(line):
  return line.split(":")[1].strip()

def format_date(date):
  d = date.isoformat().split('-')
  return d[1] + "/" + d[2] + "/" + d[0]

def get_all_dates(schedule_string, start, end):
  output = []
  schedule = schedule_string.split(',')
  day = schedule[0].strip()
  d = get_first_date_after(start, day)
  while (d <= end):
    output += [(format_date(d) + ", " + time.strip()) for time in schedule[1:]]
    d += timedelta(days=7)
  return output

def get_first_date_after(start, day):
  offset = (day_to_index(day) - start.weekday()) % 7
  return start + timedelta(days=offset)

def day_to_index(day):
  list = ['M','T','W','Th','F','Sa','S']
  return list.index(day)

def get_weekly_schedule(schedule_string):
  schedule = schedule_string.split(',')
  day_str = schedule[0].strip()
  return [(day_str + ", " + time.strip()) for time in schedule[1:]]

with open('input.txt', 'r') as reader:
  input = [line.rstrip('\n') for line in reader]
  start_date = date.fromisoformat(parse_inputline(input[0]))
  end_date = date.fromisoformat(parse_inputline(input[1]))
  weeklies_only = parse_inputline(input[2]) == 'F'

  length = len(input)
  i = 5

  output = []
  while i < length:
    if not input[i]:
      break
    parsed = get_weekly_schedule(input[i]) if weeklies_only else get_all_dates(input[i], start_date, end_date)
    output += parsed
    i += 1
  
  if not weeklies_only:
    output.sort()

  for l in output:
    print(l)
  
  with open('output.txt', 'w') as output_file:
    [(output_file.write(line+'\n')) for line in output]

print("Execution completed")