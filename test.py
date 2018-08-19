import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess
test_path = '/root/tengine/jenkins'
print(test_path)
testlist=asciitable.read(test_path+'/core_test.list')



testcase_dict=collections.OrderedDict()
for rec in testlist:
    testcase_dict[rec[0]]=rec[1]
    #pdb.set_trace()
pprint.pprint(dict(testcase_dict.items()))

#pdb.set_trace()


@pytest.mark.parametrize("id",testcase_dict.keys())
#@pytest.mark.parametrize("id",testcase_dict.keys()[1:2])
def test_eval(id):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    try:
        subprocess.check_output(test_path+"/test.sh %s"%id,shell=True)
        result=True
    except subprocess.CalledProcessError,ex:
        print ex.output # contains stdout and stderr together 
        result=False
    assert result==True