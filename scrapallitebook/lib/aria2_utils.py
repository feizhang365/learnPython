# -*- coding: utf-8 -*-

import json
import urllib2
####################
# aria2 utils
####################
__DEBUG__ = True
# __DEBUG__ = False

def log(s):
    if __DEBUG__:
        print "[LOG]:",s,"\n"
    

def arir2_call(host, port, function_name, params=None):
    url_rpc = "http://%s:%d/jsonrpc" % (host,port)

    if params==None:
        jsonreq = json.dumps({
        'jsonrpc':'2.0', 
        'id':'qwer',
        'method': function_name})
    else:
        jsonreq = json.dumps({
        'jsonrpc':'2.0', 
        'id':'qwer',
        'method':function_name,
        'params':params})
    log( jsonreq )
    
    c = urllib2.urlopen(url_rpc,jsonreq)
    r = c.read()
    log( r )
    
    return json.loads(r)
    
def arir2_multi_call(host, port, call_list):
    try:
        for call_info in call_list:
            function_name = call_info['methodName']
            if call_info.has_key('params'):
                params = call_info['params']
            else:
                params = None
    except:
        log("Please check arir2_multi_call() parameters")
        return None
        
    return  arir2_call(host, port, 'system.multicall', [call_list])
    
    
class Aria2(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        
    def __callRpc(self,function_name, params=None):
        return arir2_call(self.host, self.port, function_name, params)
        
    def version(self):
        return self.__callRpc('aria2.getVersion')
        
    def getTasks(self):
        r = arir2_multi_call(
            self.host, 
            self.port,
            [
                {'methodName':'aria2.tellActive'},
                {'methodName':'aria2.tellWaiting', 'params':[0,10000]},
                {'methodName':'aria2.tellStopped', 'params':[0,10000]}
            ])
        return r
        
    def getErrorTasks(self):
        r = self.__callRpc('aria2.tellStopped', [0,10000])
        tasks={}
        for task in r['result']:
            if task['status']=='error':
                gid= task['gid']
                #print gid
                url = task['files'][0]['uris'][0]['uri']
                #print url
                tasks[gid]=url
      
        return tasks
        
    def getActiveTasks(self):
        r = self.__callRpc('aria2.tellActive')
        tasks={}
        for task in r['result']:
            gid= task['gid']
            #print gid
            url = task['files'][0]['uris'][0]['uri']
            #print url
            tasks[gid]=url
      
        return tasks    
        
    def getWaitingAndPausedTasks(self):
        r = self.__callRpc('aria2.tellWaiting', [0,10000])
        tasks_paused={}
        tasks_waiting={}
        for task in r['result']:
            if task['status']=='paused':
                gid= task['gid']
                #print gid
                url = task['files'][0]['uris'][0]['uri']
                #print url
                tasks_paused[gid]=url
            else:
                gid= task['gid']
                #print gid
                url = task['files'][0]['uris'][0]['uri']
                #print url
                tasks_waiting[gid]=url
      
        return tasks_waiting, tasks_paused
        
    def getCompleteTasks(self):
        r = self.__callRpc('aria2.tellStopped', [0,10000])
        tasks={}
        for task in r['result']:
            if task['status']=='complete':
                gid= task['gid']
                #print gid
                url = task['files'][0]['uris'][0]['uri']
                #print url
                tasks[gid]=url
      
        return tasks
        
        
    def getUrls(self):
        r = self.getTasks()
        urls=[]
        for list in r['result']:
            for task in list[0]:
                url = task['files'][0]['uris'][0]['uri']
                urls.append(url)
        return urls
                
    def addTask(self, task_url):
        urls=self.getUrls()
        if task_url in urls:
                return None
            
        return self.__callRpc('aria2.addUri', [[task_url]])
        
        
    def addTasks(self, task_urls):
        urls=self.getUrls()
        todo=[]
        for task_url in task_urls:
            if not (task_url in urls):
                item={'methodName':'aria2.addUri', 'params':[[task_url]]}
                todo.append(item)
            
        return arir2_multi_call( self.host, self.port, todo )
        
    def restartErrorTasks(self):
        tasks = self.getErrorTasks()
        for gid in tasks:
            url= tasks[gid]
            #print gid
            #print url
            r = self.__callRpc('aria2.removeDownloadResult',[gid])
            print r
            r = self.__callRpc('aria2.addUri',[[url]])
            print r
        
    def removeTask(self,gid):
        r = self.__callRpc('aria2.removeDownloadResult',[gid])
        print r
        
    def SelectAndStartTasks(self,MAX):
        N = MAX
        
        active_task = self.getActiveTasks()
        print "Running : %d Tasks" % len(active_task)
        
        N = N-len(active_task)
        
        waiting_tasks, paused_tasks = self.getWaitingAndPausedTasks()
        print "Wating  : %d Tasks" % len(waiting_tasks)
        
        N = N-len(waiting_tasks)
        
        if N<=0:
            return
        
        list_0 = {}
        list_1 = {}
        for task in paused_tasks:
          url = paused_tasks[task]
          if url.upper().find('MOD11_L2')>0 or url.upper().find('MYD11_L2')>0:
            list_0[task]=url
          else:
            list_1[task]=url
            
        rs = []
        
        if N>0:
            for task in list_0:
                url = list_0[task]
                rs.append([task,url])
                if len(rs)>=N:
                    break
                
        N = N - len(rs)        
                
        if N>0:        
            for task in list_1:
                url = list_1[task]
                rs.append([task,url])
                if len(rs)>=N:
                    break
            
        todo=[]
        for task in rs:
            gid = task[0]
            url = task[1]
            item={'methodName':'aria2.unpause', 'params':[gid]}
            todo.append(item)
            
        return arir2_multi_call( self.host, self.port, todo )
        
if __name__ == '__main__':
    from pprint import pprint
    aria2 = Aria2("127.0.0.1",6800)
    #print(aria2.version())
    #print(aria2.getTasks())
    #print(aria2.getUrls())
    
    #print aria2.addTask('http://www.baidu.com')
    #print aria2.addTasks(['http://www.baidu.com','http://www.donews.com'])
    
    #print aria2.getErrorTasks()
    #aria2.restartErrorTasks()
    
    #print aria2.getPausedTasks()
    
    print aria2.SelectAndStartTasks(2)
    
    
    
        
    