temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


temp_hot = list(filter(lambda x: x > 28, temperatures))

max_temp = max(temp_hot)
min_temp = min(temp_hot)
average_temp = round(sum(temp_hot) / len(temp_hot), 2)

print(f"Maximal hot temperature: {max_temp}")
print(f"Minimal  hot Temperature: {min_temp}")
print(f"Average hot temperature: {average_temp}")
