def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        if (n + 1) // 2 > k or k > n:
            results.append("-1")
            continue
        
        # Find m such that the median of medians equals k
        m = (n + 1) // 2
        left_boundaries = []
        
        # Compute left boundaries for m segments
        for i in range(m):
            # Choose every second element from the middle to spread medians around k
            left_boundaries.append(2 * i + 1)
        
        results.append(str(m))
        results.append(" ".join(map(str, left_boundaries)))
    
    sys.stdout.write("\n".join(results) + "\n")
