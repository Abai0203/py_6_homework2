function selectionSort(numbers, descending = false) {
    const result = [...numbers];

    for (let i = 0; i < result.length; i++) {
        let selectedIndex = i;

        for (let j = i + 1; j < result.length; j++) {
            if (descending) {
                if (result[j] > result[selectedIndex]) {
                    selectedIndex = j;
                }
            } else {
                if (result[j] < result[selectedIndex]) {
                    selectedIndex = j;
                }
            }
        }

        [result[i], result[selectedIndex]] = [result[selectedIndex], result[i]];
    }

    return result;
}

const grades = [4, 2, 5, 3, 5, 4, 3];

console.log("Исходный список:", grades);
console.log("По возрастанию:", selectionSort(grades));
console.log("По убыванию:", selectionSort(grades, true));
