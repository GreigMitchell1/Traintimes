from nredarwin.webservice import DarwinLdbSession

darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="c879e817-1c98-4aff-9e56-977025775c3b")

count = 0

board = darwin_sesh.get_station_board('GLC')

print(darwin_sesh.get_station_board('GLC'))



while count < 10:
    info = board.train_services[count]
    print("Departure No ", count+1, info.std, " ", info.operator_name, " ",info.destination_text, "Platform: ",info.platform)

    service_id = board.train_services[count].service_id
    service = darwin_sesh.get_service_details(service_id)
    print ("This train will call at: ", [cp.location_name for cp in service.subsequent_calling_points])

    count  +=1 
