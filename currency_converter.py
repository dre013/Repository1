def main():
    print('This program converts USD to Russian ruble.')
    print()

    dollars = eval(input('Enter amount in dollars: '))

    rr = convert_to_rr(dollars)

    print('That is', rr, 'russian rubles.')

convert_to_rr = lambda dollars: dollars * 77.7

main()