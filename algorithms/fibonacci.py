def fibbonaci(n):
    sequence = [0, 1]
    
    if n<=2:
        return sequence[:n]
    
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

print(fibbonaci(10))