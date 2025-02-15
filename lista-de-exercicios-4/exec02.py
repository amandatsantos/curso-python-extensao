
# max e min da lista dec e cres
def max_min(lista):
    return max(lista), min(lista)

nums = [15, 12, 12.01, 45.9, 45.91, 8, 19, -5]
 
maior, menor = max_min(nums)


print(f"O maior número: {maior}, e o menor: {menor}")

nums.sort()
print(f"Lista crescente: {nums}")

nums.reverse()
print(f"Lista decrescente: {nums}")


