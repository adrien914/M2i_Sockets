import ecoute, queue, producteur, client, consummer

qmain = queue.Queue()

try:
    p = producteur.Producteur(qmain)
    e = ecoute.Ecoute(qmain)
except:
    pass
cli = client.Client()
cons = consummer.Consummer(cli.qmain)
cli.start()
cons.start()
p.start()
e.start()
input("")
p.stop()
e.stop()
cli.stop()
cons.stop()
