mport os
import re
def excuepath(p):
    workdir=p
    os.chdir(workdir)
    cwd=os.getcwd()
    #print 'wj:current direct:',cwd  
    dirs=os.listdir(cwd)
    print 'wj:dirs:',dirs
    for tmp in dirs:
        path=os.path.join(cwd,tmp)
        #path=cwd+'/'+tmp
        print 'wj:newpath=',path
        if os.path.isfile(path):
            if (tmp!='wj.py') & (tmp!='inkscape') &(tmp[-4:]!='.pdf')&(tmp[-4:]!='.txt'):
                data = open(path).read()
                data = re.sub('yamin','mizar', data)
                data = re.sub('Yamin','Mizar',data)
                data = re.sub('YAMIN','MIZAR',data)
                open(path, 'wb').write(data)
                newtmp=tmp.replace('yamin','mizar')
                newtmp=newtmp.replace('Yamin','Mizar')
                newtmp=newtmp.replace('YAMIN','MIZAR')
                newpath=os.path.join(cwd,newtmp)
                #newpath=cwd+'/'+newtmp 
                print 'wj:newpath:',newpath
                #_rename(path,newpath)
                os.rename(path,newpath)
        elif os.path.isdir(path):
            if (tmp[-4:]!='.git')&(tmp!='libraries'):
                print 'tmp:',tmp
                print 'tmp[0:14]',tmp[0:14]
                newtmp=tmp.replace('yamin','mizar')
                newtmp=newtmp.replace('Yamin','Mizar')
                newtmp=newtmp.replace('YAMIN','MIZAR')
                print 'cwd:',cwd
                newpath=os.path.join(cwd,newtmp)
                #newpath=cwd+'/'+newtmp                
                print 'wj:newpath:',newpath
                #_rename(path,newpath) 
                os.rename(path,newpath)
                excuepath(newpath)
if __name__=='__main__':
    excuepath(os.path.abspath('.'))
    #excuepath(os.path.abspath('.'),'Yamin','Mizar')
    #t1=Timer("excuepath(os.path.abspath('.'),old,new)","from __main__ import excuepath")
    #print t1.timeit(1)

