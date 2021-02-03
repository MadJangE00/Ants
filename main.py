# start(click button)
# time running (300 - t)
# score ( 0 + num of creatures /sec)

# create object as click
# kinds of creatures
# Queen, Jack, Normal
# objects life (birth and death) Event

# End(time over)

# 표시
# 시간
# 점수
# 개미 종류와 마리수
#
# 버튼
#
# 클릭하면 단계 넘어감

timer = 3
score = 0
ant = 1

print('time : ', timer)
print('score : ', score)
print('ant : ', ant)
print('---------------------')

while timer > 0:
    timer = timer - 1
    score = score + ant
    ant = ant + 1
    print('time : ', timer)
    print('score : ', score)
    print('ant : ', ant)
    print('---------------------')


