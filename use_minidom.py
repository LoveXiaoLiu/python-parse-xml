#_*_ coding:UTF-8 _*_
# failReRun.py     shuai_cao@netentsec.com

from xml.dom import minidom

    
def getFailtest():     # 解析output.xml文件，获取执行失败的用例，返回值为“ -t fail的用例名 -t fail的用例名”格式的字符串
    outxml = 'C:\\Users\\AutotestRecord\\autotest_log\\output.xml'
    xmldoc = minidom.parse(outxml)
    testElementList = xmldoc.getElementsByTagName('test')
    cmd = ''
    for testElement in testElementList:
        testName = testElement.getAttribute('name')
        for status in testElement.childNodes:
            if status.nodeName == 'status':
                if status.getAttribute('status') == 'FAIL':
                    # print testName
                    cmd = cmd + ' -t ' + testName
                break
    return cmd
    
def writeBAT(cmd):    #生成重跑fail脚本的bat文件
    pycmd = 'C:\Python27\python.exe -m robot.run' + cmd + ' --log log_fail.html --report report_fail.html -d C:\Users\AutotestRecord\\autotest_ReRun_log C:\RFSTestNGFW'
    fileBat = open('C:\\runbq_FAIL.bat', 'w')
    fileBat.write('c:\ncd C:\NGFW\ntitle 环境7_fail重跑\ncolor 0A\nREM 获取测试任务名称\ntclsh -encoding utf-8 AutotestFramework/gettaskname.tcl\nREM 执行用例\n')
    fileBat.write(pycmd)
    fileBat.write('\n')
    fileBat.write('REM 上传测试结果至页面展示\ncd C:\NGFW\ntclsh -encoding utf-8 AutotestFramework/run_um_fail.tcl\nexit')
    fileBat.close()
    
def writeNone():
    with open('C:\\runbq_FAIL.bat', 'w') as fileWrite:
        fileWrite.write('echo "no fail testcase"')
    
if __name__ == "__main__":
    failListCmd = getFailtest()
    if failListCmd:
        writeBAT(failListCmd.encode('gbk'))
    else:
        writeNone()