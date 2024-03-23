def view_services_serializer(service_data):

    if not isinstance(service_data,list):
        service_data=[service_data]

    sorted_data=[]
    for record in service_data:
        sorted_data.append(
            {
                "id":record.id,
                "service_name" :record.service_name,
                "description":record.description,
                "price":record.price,
                
            }
        )
        
    return sorted_data



def update_services_serializer(service_data):

    if not isinstance(service_data,list):
        service_data=[service_data]

    extra_data=[]

    for record in service_data:
        extra_data.append(
            {
                
                "service_name" :record.service_name,
                "description":record.description,
                "price":record.price,
                
            }
        )
        
    return extra_data