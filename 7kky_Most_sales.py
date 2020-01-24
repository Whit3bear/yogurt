""" You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:

    products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
    amounts: [3, 24, 8]
    prices: [199, 299, 399]

return the three product names with the highest revenue (amount * price).

Note: if multiple products have the same revenue, order them according to their original positions in the input list.
 """

def top3(products, amounts, prices):
    l = sorted([i for i in zip(products, amounts, prices)], key = lambda x: x[1]*x[2], reverse=True)     
    return [x[0] for x in l[:3]]