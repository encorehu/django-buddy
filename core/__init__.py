# -*- coding: utf-8 -*-
#from aiml import Kernel
import aiml
import os
import config as cfg
print aiml
import jieba
class TalkBot(aiml.Kernel):
    def __init__(self,properties=cfg.BOT_PROPERTIES):
        aiml.Kernel.__init__(self)
        self.verbose(cfg.DEBUG)
        #if os.path.isfile("buddy.brn"):
        #    self.bootstrap(brainFile = "buddy.brn")
        #else:
        self.init_bot()
        #    self.saveBrain("buddy.brn")
        for p in properties:
            self.setBotPredicate( p, properties[p].decode('utf-8') )
    def _processSystem(self,elem, sessionID):
        command = ""
        for e in elem[2:]:
            command += self._processElement(e, sessionID)
        #print command
        return command
    def init_bot(self):
        for file in os.listdir(cfg.AIML_SET):
            #print file
            if file[-4::]=="aiml":
                self.learn(os.path.join(cfg.AIML_SET,file) )


if __name__=="__main__":
    bot = TalkBot()
    while True:
        
        req = raw_input("> ").decode('gb18030')
        print type(req)
        if req=='exit':
            print 'Bye!'
            break
        resp = bot.respond(req)
        print resp.decode('utf-8')
