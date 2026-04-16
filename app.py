import streamlit as st
import time
import random

st.set_page_config(page_title="Algorithm Comparator", layout="centered")

st.title("⚡ Algorithm & Data Structure Comparator")

# Helper Functions

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Input Section

st.subheader(" Enter Numbers")

user_input = st.text_input("Enter numbers separated by space:", "5 3 8 2 1 5 3")

if user_input:
    numbers = list(map(int, user_input.split()))

# Sorting Comparison

st.subheader("Sorting Comparison")

if st.button("Compare Sorting Algorithms"):

    # Bubble Sort
    start = time.time()
    bubble_sorted = bubble_sort(numbers)
    bubble_time = time.time() - start

    # Merge Sort
    start = time.time()
    merge_sorted = merge_sort(numbers)
    merge_time = time.time() - start

    st.write("### Results:")
    st.write("Bubble Sort Output:", bubble_sorted)
    st.write("Merge Sort Output:", merge_sorted)

    st.success(f"Bubble Sort Time: {bubble_time:.6f} sec (O(n²))")
    st.success(f"Merge Sort Time: {merge_time:.6f} sec (O(n log n))")

# List vs Set Comparison

st.subheader(" List vs Set Membership Check")

search_value = st.number_input("Enter value to search:", value=5)

if st.button("Compare Membership Check"):

    test_list = numbers
    test_set = set(numbers)

    # List check
    start = time.time()
    found_list = search_value in test_list
    list_time = time.time() - start

    # Set check
    start = time.time()
    found_set = search_value in test_set
    set_time = time.time() - start

    st.write(f"List contains {search_value}: {found_list}")
    st.write(f"Set contains {search_value}: {found_set}")

    st.success(f"List Time: {list_time:.8f} sec (O(n))")
    st.success(f"Set Time: {set_time:.8f} sec (O(1))")

