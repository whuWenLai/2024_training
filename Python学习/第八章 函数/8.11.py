def send_messages(sender,receiver):
    while sender:
        mes=sender.pop()
        receiver.append(mes)
def show_messages(mess_list):
    for mes in mess_list:
        print(mes)
send_list=['hello','world','java']
rece_list=[]
send_messages(send_list[:],rece_list)
show_messages(send_list)
show_messages(rece_list)