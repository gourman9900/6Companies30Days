def decodedString(self, s):
        stack = []
        i = 0
        prev = ""
        while i < len(s):
            if s[i].isdigit():
                j = i
                rep = 0
                while s[j].isdigit():
                    rep = rep * 10 + int(s[j])
                    j += 1
                stack.append(rep)
                i = j
            if s[i] == "]":
                while stack[-1] != "[":
                    prev = stack.pop() + prev
                stack.pop()
                rep = int(stack.pop())
                stack.append(rep * prev)
                prev = ""
            else:
                stack.append(s[i])
            i += 1
        return stack[0]
