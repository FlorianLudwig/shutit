#The MIT License (MIT)
#
#Copyright (C) 2014 OpenBet Limited
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#ITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from shutit_module import ShutItModule
import util

class phantomjs(ShutItModule):

	def is_installed(self,shutit):
		return shutit.file_exists('/opt/phantomjs',directory=True)

	def build(self,shutit):
		shutit.set_default_expect(shutit.cfg['expect_prompts']['root_prompt'])
		shutit.send_and_expect('pushd /opt')
		shutit.install('curl')
		shutit.install('bzip2')
		# TODO: latest version of pj?
		shutit.send_and_expect('curl --insecure https://phantomjs.googlecode.com/files/phantomjs-1.9.0-linux-x86_64.tar.bz2 > phantomjs-1.9.0-linux-x86_64.tar.bz2')
		shutit.send_and_expect('bunzip2 phantomjs-1.9.0-linux-x86_64.tar.bz2')
		shutit.send_and_expect('tar -xvf phantomjs-1.9.0-linux-x86_64.tar')
		shutit.send_and_expect('ln -s phantomjs-1.9.0-linux-x86_64 phantomjs')
		shutit.send_and_expect('popd')
		return True

	def cleanup(self,shutit):
		shutit.send_and_expect('pushd /opt')
		shutit.send_and_expect('rm phantomjs-*.tar')
		shutit.send_and_expect('popd')
		return True

	def remove(self,shutit):
		shutit.send_and_expect('rm -rf /opt/phantomjs')
		return True

if not util.module_exists('shutit.tk.phantomjs.phantomjs'):
	obj = phantomjs('shutit.tk.phantomjs.phantomjs',0.319,'ShutIt phantomjs module. See http://phantomjs.org/')
	util.get_shutit_modules().add(obj)
	ShutItModule.register(phantomjs)
