#! /usr/bin/env python


class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None


class Stack(object):

    def __init__(self, min_stack=True):

        self.top = None
        self.__size = 0
        self.min_stack = min_stack
        if self.min_stack is True:
            self.__min_stack = Stack(False)

    def push(self, val):

        new_node = Node(val)
        if self.top is None:
            self.top = new_node
            if self.min_stack is True:
                self.__min_stack.push(val)
        else:
            new_node.next, self.top = self.top, new_node
            if self.min_stack is True:
                if self.top.val < self.__min_stack.top.val:
                    self.__min_stack.push(val)
        self.__size += 1

    def pop(self):
        try:
            popped, self.top = self.top.val, self.top.next
            self.__size -= 1
        except AttributeError:
            print("Uh oh!!  You're trying to pop from an empty stack")
        else:
            # if self.min_stack is True:
            #     if popped == self.__min_stack.top.val:
            #         self.__min_stack.top = self.__min_stack.top.next
            return popped

    def peek(self):
        # try:
        return self.top.val
        # except AttributeError:
        #     print("Uh oh!!  You're trying to peek from an empty stack")

    def size(self):
        return self.__size

    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False

    def sort(self):
        helper_stack = Stack()
        holder = None
        while self.top is not None:
            while holder is None:
                if self.top is None:
                    break
                if helper_stack.top is None:
                    helper_stack.push(self.pop())
                    continue
                if self.top.val >= helper_stack.top.val:
                    helper_stack.push(self.pop())
                else:
                    holder = self.pop()
            while holder is not None:
                if helper_stack.top is None:
                    self.push(holder)
                    holder = None
                    break
                if helper_stack.top.val < holder:
                    self.push(holder)
                    holder = None
                else:
                    self.push(helper_stack.pop())
        while helper_stack.__size > 0:
            self.push(helper_stack.pop())
        l = []
        i = self.top
        while i is not None:
            l.append(i.val)
            i = i.next
        return l

    def min(self):
        return self.__min_stack.top.val


class ThreeStacksInList(object):

    def __init__(self):
        self.__ls = []
        self.__s1size = 0
        self.__s2size = 0
        self.__s3size = 0

    def push(self, stack, val):
        if stack == 1:
            self.__ls.insert(0, val)
            self.__s1size += 1
        elif stack == 2:
            self.__ls.insert(self.__s1size, val)
            self.__s2size += 1
        elif stack == 3:
            self.__ls.insert(self.__s1size + self.__s2size, val)
            self.__s3size += 1

    def pop(self, stack):
        if stack == 1:
            popped = self.__ls[0]
            self.__ls.remove(0)
            self.__s1size -= 1
            return popped
        elif stack == 2:
            popped = self.__ls[self.__s1size]
            self.__ls.remove(self.__s1size)
            self.__s2size -= 1
            return popped
        elif stack == 3:
            popped = self.__ls[self.__s1size + self.__s2size]
            self.__ls.remove(self.__s1size + self.__s2size)
            self.__s3size -= 1
            return popped

    def size(self, stack):
        if stack == 1:
            return self.__s1size
        elif stack == 2:
            return self.__s2size
        elif stack == 3:
            return self.__s3size


def rev_string_with_stack(string):
    s = Stack()
    for i in range(len(string)):
        s.push(string[i])
    rs = ''
    while s.size() > 0:
        rs = rs + s.pop()
    return rs


def infix_to_postfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and (prec[opStack.peek()] >=
                                                prec[token]):
                    postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == '__main__':
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infix_to_postfix("A * ( B + C ) * D"))
