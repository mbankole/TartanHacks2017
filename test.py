data = 'potato - 3, wow - 5, fuck - 25'
adjacents = data.split(', ')
for i in range(len(adjacents)):
    adj_data = adjacents[i].split(' - ')
    adjacents[i] = {
        'name': adj_data[0],
        'distance': adj_data[1]
    }
print adjacents