#coding=utf-8
#'''conect to Tactic Server and return project,assets, shots information'''

class connectToTactic:

    def __init__(self,tacticHostName,tacticHostIP,loginID,loginPW):

        #print tacticHostName,tacticHostIP,loginID,loginPW
        self.tacticHostName = tacticHostName
        self.tacticHostIP = tacticHostIP
        self.loginID = loginID
        self.loginPW = loginPW

    def test(self,option):
        #getTacticDataB.connectToTactic(tacticHostName,tacticHostIP,loginID,loginPW)
        print 'test'
        from tactic_client_lib import TacticServerStub
        server = TacticServerStub()

        print server
        print dir(server)
        server.start("Ping Test")








    def runTactic(self,option):
        from tactic_client_lib import TacticServerStub


        #for i in sys.path:
        #    print i

        #f= open(file,'r')
      #  print scripts_path

        server = TacticServerStub(setup=False)
       # tactic_server_ip = socket.gethostbyname("vg.com")


        try:
            tactic_server_ip = socket.gethostbyname(self.tacticHostName)
        except:
            tactic_server_ip = self.tacticHostIP

        server.set_server(tactic_server_ip)
        server.set_project("simpleslot")
        ticket = server.get_ticket(self.loginID, self.loginPW)
        server.set_ticket(ticket)

        if option == 'project':
        # export projects in Tactic
            expr = "@SOBJECT(simpleslot/game)"
            projectsInTactic = server.eval(expr)
            return projectsInTactic
        elif option == 'asset':

        # export assets
            expr = "@SOBJECT(simpleslot/assets)"
            assetsInTactic = server.eval(expr)
            return assetsInTactic
        elif option == 'shot':
          #  print 'shot shot shot'
        # export shots
            expr = "@SOBJECT(simpleslot/shot)"
            shotsInTactic = server.eval(expr)
            return shotsInTactic
           # print shotsInTactic

        elif option == 'user':
         #  print 'shot shot shot'
       # export shots
            expr = "@SOBJECT(sthpw/login)"
            usersInTactic = server.eval(expr)
            return usersInTactic

    def getAssetData(self,assetsInTactic,index):
        '''get asset data ,giving index return all data'''
        assetDate =  assetsInTactic[index]

        code = assetDate['code'] #asset code
        description = (str(assetDate['description'].split('\\'))[1:-1])#.split('\\')[1:]
        timestamp = assetDate['timestamp']
        s_status = assetDate['s_status']
        keywords = assetDate['keywords']
        pipeline_code = assetDate['pipeline_code']
        frames = assetDate['frames']
        game_code = assetDate['game_code'] #project code
        assetId = assetDate['id']
        relative_dir = assetDate['relative_dir']
        name = assetDate['name']
        __search_key__ = assetDate['__search_key__']
        game_name_chn = assetDate['game_name_chn']
        login = assetDate['login']
        asset_type_code = assetDate['asset_type_code'] # process in asset,concept, model,texture,rigging

        return assetDate
        #for i in description:
        #    print i.encode('big5').decode('big5')
        #print assetDate.keys()
        #print 'code',code
        #print 'description',description#.encode('big5').decode('big5')




        #print "run getDataFromTactic End"

       # return projectsInTactic
