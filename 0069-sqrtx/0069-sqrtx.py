class Solution:
    def mySqrt(self, x: int) -> int:
        x_str = str(x)
        size = len(x_str)

        if size % 2 != 0:
            x_str = '0' + x_str  # Prepend a '0' to make the length even if not

        root = 0
        p = 0  # Part of the root found so far
        remainder = 0

        # Process each pair of digits
        for i in range(0, len(x_str), 2):
            d = 0  # Reset d for each new pair
            c = remainder * 100 + int(x_str[i:i+2])  # Calculate c using the remainder and the next pair of digits 
            
            # Find the largest d such that d * (20 * p + d) <= c
            while d * (20 * p + d) <= c:
                d += 1
            d -= 1  # Correct overshoot by decrementing d by 1

            y = d * (20 * p + d)
            remainder = c - y
            p = p * 10 + d  # Update p to include the new digit
        root = p
        return root 
