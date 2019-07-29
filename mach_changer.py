import subprocess
import optparse
import re


def get_arg():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="enter interface with this option")
    parser.add_option("-m","--mac",dest="new_mac",help="enter new mac with this option")
    return parser.parse_args()

def changer(interface,new_mac):
    subprocess.call(["ifconfig", interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig", interface,"up"])

(options,args) = get_arg()
changer(options.interface,options.new_mac)

ifconfig_result= subprocess.check_output(["ifconfig",options.interface])
verify = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
print ("new mac :" + verify.group(0))
