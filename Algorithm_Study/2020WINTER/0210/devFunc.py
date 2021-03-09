progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0 :
          # print(progresses)
          count = 0
          while progresses[0] >= 100 :
              count += 1
              progresses.pop(0)
              speeds.pop(0)
              if len(progresses) == 0 :
                  break
          if count >= 1: 
              answer.append(count)
          for i in range(len(progresses)) :
              progresses[i] += speeds[i]
    return answer

print(solution(progresses, speeds))