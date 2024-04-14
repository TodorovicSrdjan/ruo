import sys


def main():
    rmse = acc = 0
    count = len(sys.argv[1:])
    for file in sys.argv[1:]:
        with open(file) as f:
            lines = f.readlines() 
        
        curr_rmse = lines[0].split(': ')[1]
        curr_acc = lines[1].split(': ')[1]

        rmse += float(curr_rmse)
        acc += float(curr_acc.split()[0])

    rmse /= count
    acc /= count

    print("K-fold", end="\n" + 6 * '=' + '\n')
    print("Root Mean Square Error: %.2f" % (rmse))
    print(f"Accuracy: {round(acc, 2)} %")


if __name__ == "__main__":
    main()