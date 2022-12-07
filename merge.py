mds = ['./C++基础入门.md', './通讯录管理系统.md', './C++核心编程.md', './职工管理系统.md',
       './C++提高编程.md', './基于STL的演讲比赛流程管理系统.md', './机房预约系统.md']
all = []
for md in mds:
    with open(md, mode='r', encoding='utf-8') as f:
        all.extend(f.readlines())
with open("./合集.md", encoding='utf-8', mode='w') as f:
    f.writelines(all)
print("ok!")
