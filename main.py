def process_file(file_name):
    data = []
    with open(file_name) as f:
        for line in f:
            parts = line.split(',')
            data.append(parts)
          #  row = [
           #     parts[0], parts[1], parts[2]
          #  ]
            data.append(parts)
    return data


data = process_file('C:\\Users\\titov\\Desktop\\Project\\NoteData.csv')
print(data)