def main():
    calories = []
    elf_calories = []
    with open("input.txt", "r") as f:
        for line in f:
            if line.strip() == "":
                calories.append(sum(elf_calories))
                elf_calories = []
            else:
                elf_calories.append(int(line.strip()))
        calories.append(sum(elf_calories))

    max_calories = max(calories)
    max_elf = calories.index(max_calories) + 1

    print("O elfo {} está carregando mais calorias ({})".format(max_elf, max_calories))

    calories.sort(reverse=True)
    top_three_calories = calories[:3]
    total_calories = sum(top_three_calories)

    print("Os três melhores Elfos estão carregando {} calorias".format(total_calories))
    
if __name__ == "__main__":
    main()