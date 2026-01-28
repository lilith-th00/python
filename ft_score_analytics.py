import sys

print("=== Player Score Analytics ===")
n = len(sys.argv)
if n == 1:
    print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
else:
    scores = []
    try:
        for i in range(1, n):
            var = int(sys.argv[i])
            scores.append(var)
    except Exception:
        print("Caught ValueError: invalid literal for int()")
    if scores:
        print("Scores processed:", scores)
        print(f"Total players: ", len(scores))
        print("Total score:", sum(scores)) 
        print("Average score:", sum(scores)/len(scores)) 
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
        print()
#khas mazal ma2aked wach ndir try fi koula ar wela ghi wa7eda fi loop
