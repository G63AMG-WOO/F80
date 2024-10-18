stack = []
target = input()
sum = 0
n = len(target)
for i in range(n):
    if target[i] == '(':
        stack.append(target[i])
    else:
        if target[i - 1] == '(':
            stack.pop()
            sum += len(stack)
        elif target[i - 1] == ')':
            stack.pop()
            sum += 1
print(sum ,  10)
# while(True):
#         target = input()
#         if target =='.':
#             break
            
#         stack = []
#         flag = 0
        
#         for i in target:
#             if i == '(' or i =='[':
#                 stack.append(i)
#             elif i == ')':
#                 if len(stack) == 0 or stack[-1] !='(':
#                     flag = 1
#                     break
#                 elif stack[-1] == '(':
#                     stack.pop()
#             elif i == ']':
#                 if len(stack) == 0 or stack[-1] != '[':
#                     flag = 1
#                     break
#                 elif stack[-1] == '[':
#                     stack.pop()
#         if len(stack) == 0 and flag == 0:
#             print('yes')
#         else:
#             print('no')


#4949
# while(True):
#     target = input()
   

#     stack = []
#     flag = 0
#     if target == '.':
#        break
#     for i in target:
#         if i == '(' or '[':
#             stack.append(i)
#         elif i == ']':
#             if len(stack) != 0 and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 flag = 1
#                 stack.append(i)
#                 break
#         elif i == ')':
#             if len(stack) != 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 flag = 1
#                 stack.append(i)
#                 break
#     if len(stack) == 0 and flag == 0:
#         print('yes')
#     else:
#         print('no')         

# while(True):
#     word=input()

#     stack=[] # 괄호를 추가할 리스트 stack
#     if word=='.': # . 이 들어오면 종료
#         break

#     for w in word:
#         if w=='(' or w=='[': # 여는 괄호가 오면 stack에 추가
#             stack.append(w)
#         elif w==')': # ) 인 경우
#             if len(stack)!=0 and stack[-1]=='(': # stack이 비어있지 않고, 마지막 요소가 ( 이면 pop
#                 stack.pop()
#             else: # stack이 비어있거나 짝이 맞지 않으면 stack에 )을 추가하고 break
#                 # stack.append(w)
#                 break
#         elif w==']': # ] 인 경우
#             if len(stack)!=0 and stack[-1]=='[': # stack이 비어있지 않고, 마지막 요소가 [ 이면 pop
#                 stack.pop()
#             else: # stack이 비어있거나 짝이 맞지 않으면 stack에 ]을 추가하고 break
#                 # stack.append(w)
#                 break

#     if len(stack)==0: # stack이 비어있으면 모든 괄호들의 균형이 맞으므로 Yes 출력
#         print('yes')
#     else: # stack이 비어있지 않으면 괄호들의 균형이 맞지 않는 것이므로 No 출력
#         print('no')
 
        

        
# de = deque()
# for i in range(int(input())):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push_front':
#         de.appendleft(order[1])
#     elif order[0] == 'push_back':
#         de.append(order[1])
#     elif order[0] == 'pop_front':
#         if len(de) == 0:
#             print(-1)
#         else:
#             print(de.popleft())
#     elif order[0] == 'pop_back':
#         if len(de) = 0:
#             print(-1)
#         else:
#             print(de.pop())
#     elif order[0] == 'size':
#         print(len(de))
#     elif order[0] == 'empty':
#         if len(de) == 0:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'front':
#         if len(de) == 0:
#             print(-1)
#         else:
#             print(de[0])
#     elif order[0] == 'back':
#         if len(de) == 0:
#             print(-1)
#         else:
#             print(de[len(de) - 1])
