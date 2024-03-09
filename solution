def get_input_adat():
    pozicio_1 = int(input("Írd be az első 1-es indexét (0-99): "))
    pozicio_2 = int(input("Írd be az második 1-es indexét (0-99): "))
    pozicio_3 = int(input("Írd be az harmadik 1-es indexét (0-99): "))

    adat = [0] * 100
    adat[pozicio_1] = adat[pozicio_2] = adat[pozicio_3] = 1
    return adat


arr = get_input_adat()

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

    for i in range(40, 97, 3):
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
        remaining_indices =[i for i in range(0, 39) if i not in excluded_indices]
        for i in range (0, len(remaining_indices)-3, 4):
            comp_result = compare(i, i+1)
            if comp_result == ">":
                found_indices.append(i)
                found_indices.append(i+1)
                excluded_indices.update({i, i+1})
            elif comp_result == "<":
                found_indices.append(i+2)
                found_indices.append(i+3)
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


eredmeny = find_ones(arr)
print("Comparisons made:", eredmeny["comparisons"])
print("Total comparisons:", eredmeny["total_comparisons"])
print("Indices of 1s:", eredmeny["found_indices"])


    

if __name__ == "__main__":
    find_ones(arr)
