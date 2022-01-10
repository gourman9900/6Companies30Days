def colName (self, n):
        def dfs(n):
            if n == 0:return ""
            if n < 27:return chr(96 + n)
            return dfs(n//26 if n % 26 != 0 else (n//26) - 1) + (chr(96 + (n%26 if n % 26 != 0 else 26)))
        return dfs(n).upper()
