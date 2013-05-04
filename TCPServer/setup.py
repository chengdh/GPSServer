#coding=utf-8
import sys
from twisted.python import log
from twisted.python import logfile
from twisted.internet import protocol, reactor
from twisted.internet.interfaces import IListeningPort
import config
import time,os,threading,datetime

from SqlOpration import SqlOprate

lastDic={}
lastPortDic={}
configChangTime=''
stateChangTime=''

def stop():
    reactor.stop()

def changState():
    try:
        statinfo = os.stat('state.txt')
        mtime=time.localtime(statinfo.st_mtime)
        fileTime=datetime.datetime(mtime[0],mtime[1],mtime[2],mtime[3],mtime[4],mtime[5])
        global stateChangTime
        if stateChangTime!=fileTime:
            stateChangTime=fileTime
            return True
        
        return False
    except Exception as e:
        log.err()


def changConfig():
    try:
        statinfo = os.stat('config.py')
        mtime=time.localtime(statinfo.st_mtime)
        fileTime=datetime.datetime(mtime[0],mtime[1],mtime[2],mtime[3],mtime[4],mtime[5])
        global configChangTime
        if configChangTime!=fileTime:
            configChangTime=fileTime
            return True
    
        return False
    except Exception as e:
        log.err()

def serverPortRepeate(k,port):
    for key in config.dic:
        if k!=key:
            d=config.dic[key]
            if d['enable'] and port==d['serverPort']:
                log.msg('端口设定重复请更改！\n')
                #print('端口设定重复请更改！')
                return True
    return False

def update():
    
    try:
        if changState():
            f=open('state.txt')
            try:
                ft=f.read()
                if ft=='stop':
                    stop()
                print(ft)
            finally:
                    f.close()
        if not changConfig():
            reactor.callLater(30,update)
            return
        #重新载入配置文件
       
        reload(config)
        print(config.dic)
        #源配置信息和现在的数据进行对比
        SqlOprate.updateGpsClearDay(config.gpsTableClearTime)
        SqlOprate.updateAlmClearDay(config.almTableClearTime)
        for key in config.dic:
            dic=config.dic[key]
            if dic and dic['enable']:
            
                if key in lastDic:
                    laD=lastDic[key]
                    factory=dic['factory']
                    if laD['serverPort']!=dic['serverPort'] and not serverPortRepeate(key,dic['serverPort']):
                        listeningPort=lastPortDic[key]
                        listeningPort.stopListening()
                        factory.killAllConnection()
                        del lastPortDic[key]
                        listeningPort=reactor.listenTCP(dic['serverPort'], factory)
                    
                        lastPortDic[key]=listeningPort
                        
                
                    if laD['mysqlHost']!=dic['mysqlHost'] or laD['mysqlUser']!=dic['mysqlUser'] or laD['db']!=dic['db'] or laD['unpn_history']!=dic['unpn_history']:
                    
                  
                    
                        connUnpn,cursorUnpn=SqlOprate.sqlGetUnpnConnection(key)
                        connUnpnhis,cursorUnpnhis=SqlOprate.sqlGetUnpnhisConnection(key)
                    
                        SqlOprate.sqlUnpnConnect(key,dic)
                        SqlOprate.sqlUnpnhisConnect(key,dic)
                
                        SqlOprate.sqlLostUnpnConnect(key,connUnpn,cursorUnpn)
                   
                        SqlOprate.sqlLostUnpnhisConnect(key,connUnpnhis,cursorUnpnhis)
                    
                   
                
                else:
                    if not serverPortRepeate(key,dic['serverPort']):
                        factory=dic['factory']
                        listeningPort=reactor.listenTCP(dic['serverPort'], factory)
                        lastPortDic[key]=listeningPort
                        SqlOprate.sqlUnpnConnect(key,dic)
                        SqlOprate.sqlUnpnhisConnect(key,dic)
                #更新源配置信息
                lastDic[key]=dic
            elif dic and not dic['enable']:
                if key in lastDic:
                    #关闭不用的数据库连接
                    connUnpn,cursorUnpn=SqlOprate.sqlGetUnpnConnection(key)
                    connUnpnhis,cursorUnpnhis=SqlOprate.sqlGetUnpnhisConnection(key)
                
                    SqlOprate.sqlLostUnpnConnect(key,connUnpn,cursorUnpn)
                    
                    SqlOprate.sqlLostUnpnhisConnect(key,connUnpnhis,cursorUnpnhis)
                    #关闭不用的监听套接口
                    listeningPort=lastPortDic[key]
                    listeningPort.stopListening()
                
                    d=lastDic[key]
                    f=d['factory']
                    f.killAllConnection()
                    #删除此键
                    del lastDic[key]
                    del lastPortDic[key]
                
        #如果源数据中没有现在的配置信息中的对应键 源配置更新回将现在没有的键值删除
        dicTemp=lastDic.copy()
        for key in dicTemp:
            if key not in config.dic:
                
                #关闭不用的数据库连接
            
                connUnpn,cursorUnpn=SqlOprate.sqlGetUnpnConnection(key)
                connUnpnhis,cursorUnpnhis=SqlOprate.sqlGetUnpnhisConnection(key)
            
                SqlOprate.sqlLostUnpnConnect(key,connUnpn,cursorUnpn)
                SqlOprate.sqlLostUnpnhisConnect(key,connUnpnhis,cursorUnpnhis)
                #关闭不用的监听套接口
                listeningPort=lastPortDic[key]
                listeningPort.stopListening()
            
                d=lastDic[key]
                f=d['factory']
                f.killAllConnection()
                #删除此键
                del lastDic[key]
                del lastPortDic[key]
        del dicTemp
    except Exception as e:
        log.err()

    reactor.callLater(30,update)


#--Main--#
def main():
    log.startLogging(open("./log/sysLog.log",'w'))
    #log.startLogging(sys.stdout)
    #f = logfile.DailyLogFile("dailylog", "./log")
    #log.startLogging(f)
    for key in config.dic:
        dic=config.dic[key]
        if dic and dic['enable']:
            factory=dic['factory']
            if factory and not serverPortRepeate(key,dic['serverPort']):
                iPort= reactor.listenTCP(dic['serverPort'], factory)
                lastPortDic[key]=iPort
                lastDic[key]=dic
    
    reactor.run()

main()



        







        
