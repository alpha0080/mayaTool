
#import sys
def getDataFromTactic(self):
   # import sys
    print "run getDataFromTactic start"
    scripts_path = "//mcd-one/database/assets"
    sys.path.append(scripts_path +  "/client")
    sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")
    from tactic_client_lib import TacticServerStub

    server = TacticServerStub(setup=False)
   # tactic_server_ip = socket.gethostbyname("vg.com")
    
    
    try:
        tactic_server_ip = socket.gethostbyname("vg.com")
    except:
        tactic_server_ip = "192.168.163.60"


    server.set_server(tactic_server_ip)
    server.set_project("simpleslot")
    ticket = server.get_ticket("julio", "1234")
    server.set_ticket(ticket)

    # export projects in Tactic
    expr = "@SOBJECT(simpleslot/game)"
    projectsInTactic = server.eval(expr)


    # export assets
    expr = "@SOBJECT(simpleslot/assets)"
    assetsInTactic = server.eval(expr)

    # export shots
    expr = "@SOBJECT(simpleslot/shot)"
    shotsInTactic = server.eval(expr)
    print "run getDataFromTactic End"
    