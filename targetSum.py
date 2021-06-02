def targetSum(array, target_sum):
    return findCombination(array, [], target_sum)

def findCombination(array, combination, target):
    #Base cases: 
    if(target == 0): #if combination found
        return combination
    if(target < 0 or len(array) <= len(combination)): #if no combination found
        return []
    #recursive steps: 
    combo = combination.copy()
    combo.append(array[len(combination)])
    newCombo1 = findCombination(array, combo, target-array[len(combination)]) #try adding first element to combination
    if(newCombo1 != []):
        return newCombo1
    newCombo2 = findCombination(array[1:], combination, target) #try removing first element from array
    return newCombo2


array = [2,7,11,15]
print(targetSum(array, 9))