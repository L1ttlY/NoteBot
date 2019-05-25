def process_file(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            parts = line.split()
            data.append(parts)
          #  row = [
           #     parts[0], parts[1], parts[2]
          #  ]
            data.append(parts)
    return data


data = process_file('NoteData.csv')
print(data)


# def telegram_bot():
# There should be code for telegram bot :p(work in progress)
