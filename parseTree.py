from trees import BinaryTree
from stack import Stack

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    print(eTree)
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            # print(pStack.size())
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    print(currentTree)
    # print(pStack.size())
    # p = pStack.pop()
    # print(p.getRootVal())
    return eTree



if __name__ == '__main__':
    # pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    pt = buildParseTree("( 3 +")


# ['(', '3', '+', '(', '4', '*', '5' ,')',')']