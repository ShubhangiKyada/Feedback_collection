
def getuser_serializer(users_data):
    if not isinstance(users_data,list):
        users_data=[users_data]

    extra_data=[]

    for record in users_data:
        extra_data.append(
            {
                "fname":record.first_name,
                "lname" :record.last_name,
                "name":record.name,
                "email":record.email,
                "phone_no":record.phone_no,
                "active":record.is_active,
                "verify":record.is_verify,
                
            }
        )
        
    return extra_data

#create validator serializer

def  user_detail_serializer(users_data):
    if not isinstance(users_data,list):
        users_data=[users_data]
    users_data=users_data[0]

    sorted_data={
        "id":users_data.id,
        "name":users_data.name,
        "email":users_data.email,
        "phone_no":users_data.phone_no,
        "role":users_data.role,
    }
    return sorted_data
