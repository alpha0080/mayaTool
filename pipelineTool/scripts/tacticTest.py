def runTactic(option,tacticHostName,tacticHostIP,loginID,loginPW):
    from tactic_client_lib import TacticServerStub


    #for i in sys.path:
    #    print i

    #f= open(file,'r')
  #  print scripts_path

    server = TacticServerStub(setup=False)
   # tactic_server_ip = socket.gethostbyname("vg.com")
    
    
    try:
        tactic_server_ip = socket.gethostbyname(tacticHostName)
    except:
        tactic_server_ip = tacticHostIP


    server.set_server(tactic_server_ip)
    server.set_project("simpleslot")
    ticket = server.get_ticket(loginID, loginPW)
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
    # export shots
        expr = "@SOBJECT(simpleslot/shot)"
        shotsInTactic = server.eval(expr)
        return shotsInTactic
    #print "run getDataFromTactic End"
    
   # return projectsInTactic
    