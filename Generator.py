def count(start, step):
    while True:
        yield start
        start += step
    counter = count(10, 2)
    print(next(counter), next(counter), next(counter))
    
if __name__ == "__counter__":
    print(counter)


