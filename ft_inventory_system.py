alice_inventory = {
    "sword" :{
        "category" : "weapon",
        "rarity" : "rare",
        "quantity" : 1,
        "value" : 500
    },
    "potion" :{
        "category" : "consumable",
        "rarity" : "common",
        "quantity" : 5,
        "value" : 50
    },
    "shield" :{
        "category" : "armor",
        "rarity" : "uncommon",
        "quantity" : 1,
        "value" : 200
    }
}
bob_inventory = {
    "potion" : {
        "category" : "consumable",
        "rarity" : "common",
        "quantity" : 0,
        "value" : 50
    }
}
print("=== Player Inventory System ===\n")

value = 0
count  = 0
for key, data in alice_inventory.items():
    total = data["quantity"] * data["value"]
    value += total
    count += data["quantity"]
    print(f"{key} ({data["category"]}, {data["rarity"]}):"
            f" {data["quantity"]}x @ {data["value"]} gold each =  {total} gold")
print()

print(f"Inventory value: {value} gold")
print(f"Item count: {count} items")

result_list = []
count_list = []
for key, data in alice_inventory.items():
    result_list.append(data["category"])
    count_list.append(data["quantity"])
print("Categories: ", end="")
for x in range(len(result_list)):
    if x + 1 != len(result_list):
        print(f"{result_list[x]}({count_list[x]}), ", end="")
    else:
        print(f"{result_list[x]}({count_list[x]})")
print()

print("=== Transaction: Alice gives Bob 2 potions ===")
transfer = 2
if alice_inventory["potion"]["quantity"] >= transfer:
    alice_inventory["potion"]["quantity"] -= transfer
    bob_inventory["potion"]["quantity"] += transfer
    print("Transaction successful!")
print()

print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inventory["potion"]['quantity']}")
print(f"Bob potions: {bob_inventory["potion"]["quantity"]}")
print()

print("=== Inventory Analytics ===")
value = 0
count  = 0
for key, data in alice_inventory.items():
    total = data["quantity"] * data["value"]
    value += total
    count += data["quantity"]
print(f"Most valuable player: Alice ({value} gold)")
print(f"Most items: Alice ({count} items)")
print("Rarest items: sword")
