# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.product_price = {}
        for i in range(len(self.products)):
            self.product_price[self.products[i]] = self.prices[i]      

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = 0
      
        for i in range(len(product)):
            total += self.product_price[product[i]] * amount[i]
            product 
        if self.count%self.n != 0:
            return total
        else:
            return total * ((100 - self.discount) / 100)



        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)