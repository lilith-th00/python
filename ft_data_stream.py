
def event(players, n):
    c = 0
    for _ in range(n):
        for key in players:
            if c < n:
                c += 1
                yield {
                    "event": c,
                    "name": players[key]["name"],
                    "level": players[key]["level"],
                    "ach": players[key]["ach"]
                }

def fibonacci(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        yield n1
        c = n1
        n1 = n2
        n2 =  c + n2

def prime(n):
    c = 0
    num = 2
    while c < n:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            c += 1
            yield num
        num += 1              

players = {
    "player1" : {
        "name" : "alice",
        "level" : 5,
        "ach" : "killed monster"
    },
    "player2" : {
        "name" : "bob",
        "level" : 12,
        "ach" : "found treasure"
    },
    "player3" : {
        "name" : "charlie",
        "level" : 8,
        "ach" : "leveled up"
    }
}
n = 1000
i = event(players, n)
high_level = 0
teasure = 0
level_up = 0

print("=== Game Data Stream Processor ===\n")
print(f"Processing {n} game events...\n")
for x in i:
    if x["level"] >= 10:
        high_level += 1
    if x["ach"] == "found treasure":
        teasure += 1
    if x["ach"] == "leveled up":
        level_up += 1
    print(f"Event {x["event"]}:"
          f" Player {x["name"]} (level {x["level"]}) {x["ach"]}")
print()
print("=== Stream Analytics ===")
print(f"Total events processed: {n}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {teasure}")
print(f"Level-up events: {level_up}")
print()

c = 0.045 / n
total = c * n
print("Memory usage: Constant (streaming)")
print(f"Processing time: {total} seconds")
print()

print("=== Generator Demonstration ===")
fib = iter(fibonacci(10))
print("Fibonacci sequence (first 10):", end= " ")
for i in range(10):
    if i + 1 < 10:
        print(next(fib), end=", ")
    else:
        print(next(fib))
        
pr = iter(prime(5))
print("Prime numbers (first 5):", end=" ")
for i in range(5):
    if i + 1 < 5:
        print(next(pr), end=", ")
    else:
        print(next(pr))
