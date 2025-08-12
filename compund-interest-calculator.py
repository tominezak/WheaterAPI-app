principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the priciple amount: '))
    if principle <= 0:
        print('not possible')

while rate <= 0:
    rate = float(input('Enter the rate amount: '))
    if rate <= 0:
        print('not possible')

while time <= 0:
    time = int(input('Enter the time amount: '))
    if time <= 0:
        print('not possible')

print(principle)
print(rate)
print(time)

total = principle * pow(1 + rate / 100, time)
print(f'Balance after {time} years: {total:.2f}')