from itertools import combinations

def find_ones(arr):
    comparisons = []
    found_indices = []
    excluded_indices=set()
    
    def compare(i, j):
        comparisons.append((i,j))
        if arr[i] > arr[j]:
            return ">"
        elif arr[i] < arr[j]:
            return "<"
        else:
            return "="

    # Initial search among first 40 (in pairs) and last 60 (in trios)
    for i in range(0, 39, 2):
        comp_result = compare(i, i+1)
        if comp_result == ">":
            found_indices.append(i)
            excluded_indices.update({i, i+1})
        elif comp_result == "<":
            found_indices.append(i+1)
            excluded_indices.update({i, i+1})
    if len(found_indices) == 3:
        return {"comparisons": comparisons, "total_comparisons": len(comparisons), "found_indices": found_indices}

    for i in range(40, 98, 3):
        comp_result1 = compare(i, i+1)
        comp_result2 = compare(i+1, i+2)
        if comp_result1 != "=" or comp_result2 != "=":
            if arr[i] == 1:
                found_indices.append(i)
            if arr[i+1] == 1:
                found_indices.append(i+1)
            if arr[i+2] == 1:
                found_indices.append(i+2)

    if len(found_indices) == 3:
        return {"comparisons": comparisons, "total_comparisons": len(comparisons), "found_indices": found_indices}


 
    # Logic to find remaining ones if not all were found
    if len(found_indices) == 1:
        remaining_indices = [i for i in range(0, 39) if i not in excluded_indices] 
        for i in range(0, len(remaining_indices) - 3, 4):
            comp_result = compare(remaining_indices[i], remaining_indices[i+2])
            if comp_result == ">":
                found_indices.append(remaining_indices[i])
                found_indices.append(remaining_indices[i+1])
            elif comp_result == "<":
                found_indices.append(remaining_indices[i+2])
                found_indices.append(remaining_indices[i+3])
            if len(found_indices) == 3:
                return {"comparisons": comparisons, "total_comparisons": len(comparisons), "found_indices": found_indices}
            
            
    elif len(found_indices) == 0:
        for i in range(40, 97, 6):
            comp_result = compare(i, i+3)
            if comp_result == ">":
                found_indices.extend([i, i+1, i+2])
                break
            if comp_result == "<":
                found_indices.extend([i+3, i+4, i+5])
                break
                
                
    return {"comparisons": comparisons, "total_comparisons": len(comparisons), "found_indices": found_indices}

def generate_arrays():
    for indices in combinations(range(100), 3):
        arr = [0] * 100
        for index in indices:
            arr[index] = 1
        yield arr, set(indices)

def test_find_ones():
    results = []
    for arr, correct_indices in generate_arrays():
        result = find_ones(arr)
        found_indices = set(result['found_indices'])
        total_comparisons = result['total_comparisons']
        
        if found_indices != correct_indices or total_comparisons >= 74:
            results.append((False, arr, found_indices, correct_indices, total_comparisons))
        else:
            results.append((True, arr, found_indices, correct_indices, total_comparisons))
    return results

results = test_find_ones()
failed_cases = [result for result in results if not result[0]]

if not failed_cases:
    print("All tests passed.")
else:
    print(f"Number of failed cases: {len(failed_cases)}")
    # Optionally, print details for each failed case
    for case in failed_cases[:100]:  # Print details for the first 5 failed cases to avoid too much output
        _, arr, found_indices, correct_indices, total_comparisons = case
        print(f"Test failed for array: {arr}")
        print(f"Found indices: {found_indices}, Correct indices: {correct_indices}")
        print(f"Total comparisons: {total_comparisons}")
