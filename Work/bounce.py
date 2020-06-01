# bounce.py
#
# Exercise 1.5

if __name__ == '__main__':
    height = 100
    bounce_count = 0

    while bounce_count < 10:
        height = height * 3/5
        bounce_count += 1
        print(f'{bounce_count} {round(height, 4)}')
