"""write a function called linear_search_products and a target product name is input.
The function should perform a linear search to find and target product in the list and return a list of all occurrences of the product if found,or an empty list if the product is not found."""
def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product,in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
# example usage:
products =["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products,target2)
print(result)