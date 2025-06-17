def hours_to_minuits_seconds(hour):
    minuits = hour * 60
    seconds = minuits * 60
    return minuits,seconds

def main():
    print("Enter a hours ")
    k = hours_to_minuits_seconds(int(input()))
    print(f"minuits are: {k[0]}\nseconds are: {k[1]}")

if __name__ == '__main__':
    main()
