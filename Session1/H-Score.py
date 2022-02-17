def h_index(n, citations):
    ans = []
    # TODO: Complete the function to get the H-Index scores after each paper

    lsCitations = list(citations)

    for i in range(n):
        # print(i)
        # print(lsCitations[i])
        if i == 0:
            ans.append(1)
            # print('ans1=',ans)
        elif i+1 == lsCitations[i]:
            ans.append(i)
            # print('ans2=',ans)
        elif i+1 == n:
            tmp = ans.pop()
            ans.append(tmp)
            ans.append(tmp+1)
            # print('ans4=',ans)
        else:
            tmp = ans.pop()
            ans.append(tmp)
            ans.append(tmp)
            # print('ans3=',ans)

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        # The number of citations for each paper
        citations = map(int, input().split())
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " +
              ' '.join(map(str, h_index_scores)))
