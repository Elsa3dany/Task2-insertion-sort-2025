def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:  # Change comparison for descending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function
book_prices = [12.99, 25.50, 8.75, 19.99, 30.00, 15.20]
sorted_prices = insertion_sort_desc(book_prices)
print("Book prices sorted in descending order:", sorted_prices)
