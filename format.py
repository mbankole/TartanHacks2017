import io, numpy as np
supe = """
UC MAIN  <40.44321,-79.94225, 950.2>
UC ROUND  <40.44322,-79.94144, 948.4>
WIEGAND  <40.44412,-79.94219, 949.8>
PURNELL ROUND <40.44316,-79.94365, 947.8>
PURNELL NW <40.44391,-79.94325, 947.7>
SKIBO N <40.44125,-79.94145, 960.8>
SKIBO W <40.44074,-79.94157, 975.1>
SKIBO E (q) <40.44096,-79.94108, 975>
CFA S (A q) <40.44124,-79.94305, 966>
CFA W (q) <40.44164,-79.94319,966>
CFA N (A) <40.44196,-79.94286,966>
"""
# HUNT LIBRARY MAIN <40.44133,-79.94374, 966.5>
# HUNT LIBRARY S <40.44099,-79.94402, 964.3>
# TEPPER N <40.44161,-79.94210, 956.4>
# TEPPER SW <40.44085,-79.94224, 972>
# TEPPER SE <40.44073,-79.94293, 969.2>
# BAKER W <40.44132,-79.94422, 964.7>
# BAKER N (qA) <40.44157,-79.94461, 959.3>
# BAKER N (q) <40.44164,-79.94511, 956.3>
# BAKER N (q) <40.44173,-79.94556, 949.7>
# PORTER N (A) <40.44205,-79.94610, 937.6>
# PORTER SW (E) <40.44147,-79.94591, 942.2>
# WEAN S (q) <40.44241,-79.94599, 937.6>
# DOHERTY MAIN <40.44232,-79.94389, 962.7>
# DOHERTY E (A) <40.44249,-79.94412, 916.5>
# DOHERTY W (A) <40.44258,-79.94507, 915.8>
# DOHERTY S (A B) <40.44227,-79.94441, 916>
# DOHERTY N © <40.44276,-79.94414, 897.7>
# RESNIK ROUND <40.44237,-79.93969, 948>
# RESNIK E <40.44262,-79.94044, 948>
# RESNIK NE <40.44271,-79.94026, 948>
# WEST WING W <40.44265,-79.94059, 948>
# WEST WING E <40.44276,-79.94114, 947.4>
# MARGARETMORRISON N <40.44265,-79.94143, 948.5>
# MARGARETMORRISON ROTUNDA <40.44183,-79.94156, 945.7>
# WIEGAND N <40.44369,-79.94158, 949.5>
# SCOTT <40.44274,-79.94664, 896.2>
# GATES BRIDGE <40.44326,-79.94448, 886.3+15*4>
# GATES N  <40.44370,-79.94445, 904.2>
# GATES q E <40.44354,-79.94495, 905.5>
# GATES q S <40.44309,-79.94483, 878.1>
# HEINZ N <40.44442,-79.94555, 910.3>
# HEINZ SW <40.44387,-79.94509, 906>
# NEWELLSIMON N <40.44365,-79.94552, 905.3>
# NEWELLSIMON W (q) <40.44341,-79.94601, 875.4>
# NEWELLSIMON E (q) <40.44318,-79.94525, 875.2>
# 
supe.strip()
supe.splitlines()
super=""
for val in supe: super+=val

output=""
i=0
dict = {}
cNDEG = 40.44183
cWDEG = -79.94156
currname=""
for c in super:
    if c=='<':
        dict[currname]=i
        currname=""
        i+=1
    if c in '+*-0123456789,>.':
        output+=c
    elif c in '\<n': continue
    else: currname+=c
output = output.split('>')
output=[output[i].split(',') for i in range(len(output))]
temp=[]
onetothree=0
i=0
for vec in output:
    for val in vec:
        try:temp+=[float(eval(val))]
        except:
            continue
        onetothree+=1
        if onetothree==3: 
            for key in dict:
                if dict[key] == i:
                    dict[key]=temp
            temp=[]   
            onetothree=0 
            i+=1
# with open("Output.txt", "w") as text_file:
#      text_file.write(str(dict))

bigList=[]
for name in dict:

    bigList+=[{'name':name,'coords':dict[name]}]
np.save('nodeVecDict.npy', dict)
np.save('bigList.npy',{0:bigList}) 
