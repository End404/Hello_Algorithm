
# 315 有序表抽象数据类型及Python实现

'''
抽象数据类型：有序表OrderedList
❖ OrderedList所定义的操作如下：

    OrderedList()：创建一个空的有序表

    add(item)：在表中添加一个数据项，并保持整体顺序，此项原不存在.

    remove(item)：从有序表中移除一个数据项，此项应存在，有序表被修改.

    search(item)：在有序表中查找数据项，返回是否存在.

    isEmpty()：是否空表.

    size()：返回表中数据项的个数.

    index(item)：返回数据项在表中的位置，此项应存在.

    pop()：移除并返回有序表中最后一项，表中应至少存在一项.

    pop(pos)：移除并返回有序表中指定位置的数据项，此位置应存在.

'''


# 有序表实现：add方法
def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        #发现插入位置
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()
    
    temp = Node(item)
    #插入在表头
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        #插入在表中
        temp.setNext(current)
        previous.setNext(temp)


    

        