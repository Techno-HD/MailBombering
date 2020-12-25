import smtplib, time
import tkinter as tk

def sending():
	port = 587
	s_server='smtp.gmail.com'
	sender=sender_id.get()
	receiver=receiver_id.get()
	password=passwd.get()
	loop=int(iteration.get())
	
	message=question.get("1.0", "end").rstrip()

	server=smtplib.SMTP(s_server,port)
	server.starttls()
	server.login(sender,password)
	for i in range(loop):
		server.sendmail(sender,receiver,message)
		print('{} sent successfully'.format(i+1))
		x='{} sent successfully'.format(i+1)
		final.config(text=x)
		final.update()
		time.sleep(1)
	# server.sendmail(sender,receiver,'If you get this mail then whatsapp me.....')
	print('Task is completed............')
	x='Task is completed............'
	final.config(text=x)
	final.update()

root=tk.Tk()
root.title('MailBombering')
root.geometry('400x300')
root.resizable(0,0)

l_sender=tk.Label(root,text='Sender ID')
l_sender.grid(row=0,column=0,padx=5,pady=5)
sender_id=tk.Entry(root)
sender_id.grid(row=0,column=1,padx=5,pady=5)

l_pass=tk.Label(root,text='Password')
l_pass.grid(row=0,column=2,padx=5,pady=5)
passwd=tk.Entry(root,show='*')
passwd.grid(row=0,column=3,padx=5,pady=5)

l_receiver=tk.Label(root,text='Receiver ID')
l_receiver.grid(row=1,column=0,padx=5,pady=5)
receiver_id=tk.Entry(root)
receiver_id.grid(row=1,column=1,padx=5,pady=5)

l_iteration=tk.Label(root,text='No. of message')
l_iteration.grid(row=1,column=2,padx=5,pady=5)
iteration=tk.Entry(root)
iteration.grid(row=1,column=3,padx=5,pady=5)

question=tk.Text(root,height=4,width=49)
question.place(x=0,y=70)
question.insert(tk.INSERT, "Enter the message here.....")

send=tk.Button(root,text='Send',command=sending)
send.place(x=190,y=150)

final=tk.Label(root)
final.place(x=0,y=170)

root.mainloop()
