#分析问题,明确结果
#思考需要的知识,或搜索新知识
#思考切入点
#尝试解决问题的一部分
#重复1-4步
import math

def workhours():
    project_size=float(input('请输入项目大小'))
    worker=int(input('请输入工作人数'))
    workhour=project_size*80/worker
    print('完成项目需要%.1f工时' %workhour)

def workers():
    project_size=float(input('请输入项目大小'))
    workhour=float(input('请输入工时时限'))
    worker=math.ceil(project_size/80/workhour)
    print('完成项目需要{}人'.format(int(worker)))

choice=input('请输入计算选项:\n1为计算工作时间\n2为计算工作人数')
if choice =='1':
    workhours()
elif choice=='2':
    workers()
else:
    print('输入有误,请重新输入')

#---------------合并workhours(),worker()------------
def cost(project_size,workhours=None,workers=None):
    if workers == None:
        worker=math.ceil(project_size/80/workhours)
        print('完成项目需要{}人'.format(int(worker)))
    else:
        workhour=project_size*80/workers
        print('完成项目需要%.1f工时' %workhour)

i=input('请选择您要计算的类型:\n1-人力计算\n2-工时计算')
if i == '1':
    workhour=float(input('请输入工时'))
    size=float(input('请输入项目大小'))
    cost(workhours=workhour,project_size=size)
else:
    worker=int(input('请输入人力数量'))
    size=float(input('请输入项目大小'))
    cost(workers=worker,project_size=size)

