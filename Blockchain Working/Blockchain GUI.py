# M Farooq BSCS 5th 19064
# Blockchain GUI Application
import BlockChain as BC
from tkinter import messagebox as Msg
import tkinter as tk
from tkinter import font
import hashlib
import datetime as dt

# =========Root window and Blockchain Objects=========
#region
MyBC = BC.Blockchain()
Range = 0 #MyBC.get_ind()
PageNo = MyBC.get_ind()-1
print('PageNo Value : ', PageNo)
NxtP = MyBC.find_block(PageNo)
PreP = MyBC.find_block(PageNo - 1)
for i in range(Range):
    Bd = MyBC.Chain[i]
    print('Block Index   : ', Bd.index)
    print('Time Stamp  : ',Bd.timstp)
    print('Block Data     : ',  Bd.data)
    print('PrevHash       : ',  Bd.PrevH)
    print('Nonce Value : ', Bd.nonce)
    print('Current Hash : ', Bd.Hash)
    print()
# Creating Tk Object
window = tk.Tk()
window.title('Blockchain GUI')
window.geometry('1190x700')
window.minsize(1190, 690)
window.configure(bg='#333333')
Font_Path = 'C:/Windows/Fonts/JetBrainsMono-Regular.ttf'
Myfont= font.Font(family='JetBrains Mono',  size=12, weight='bold')
gldata = ''
fonts = [
    "JetBrains Mono", "Arial", "Helvetica", "Times New Roman", "Courier New", "Verdana", "Georgia", "Impact", "Tahoma", "Trebuchet MS",
    "Arial Black", "Comic Sans MS", "Century Gothic", "Palatino Linotype", "Lucida Console", "Lucida Sans Unicode",
    "Garamond", "Book Antiqua", "Calibri", "Candara", "Consolas", "Cambria", "Franklin Gothic Medium", "Arial Narrow",
    "Baskerville", "Futura", "Segoe UI", "Helvetica Neue", "Roboto", "Open Sans", "Montserrat", "Lato", "PT Sans",
    "Raleway", "Oswald", "Ubuntu", "Playfair Display", "Source Sans Pro", "Noto Sans", "Droid Sans", "Merriweather",
    "Avenir", "Didot", "Rockwell", "Myriad Pro", "Century", "Courier", "Monaco", "Optima", "Trajan", "Bodoni",
    "Gill Sans"
]
#endregion

# =============Menu Bar============
# region
menubar = tk.Menu(window)
window.config(menu=menubar)
Home_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=Home_menu, label='Home')
Hash_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=Hash_menu, label='Blockchain')
Explorer_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=Explorer_menu, label='Exit')

#endregion

# ============Frames in Window============
# region
left_frame = tk.Frame(window, width=217, height=700, bg='grey')
left_frame.grid(row=0, column=0, padx=5, pady=5)
left_frame.grid_propagate(False)

global right_frame
right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
right_frame.grid(row=0, column=1, padx=5, pady=5)
right_frame.grid_propagate(False)

bottom_frame = tk.Frame(window, width=1578, height=90, bg='grey')
bottom_frame.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
# endregion

# ===========Menus in Left Frame==========
# Menus in Left farme
# region
tk.Label(left_frame, text=' Blockchain \nWorking', fg='black', font= (fonts[11], 25, "bold")  ).grid(row=0, column=0, padx=5, pady=8)

Hash_btn = tk.Button(left_frame, text='Hash', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 25')
Hash_btn.grid(row=2, column=0, padx=1, pady=1)
Block_btn = tk.Button(left_frame, text='Block', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24')
Block_btn.grid(row=3, column=0, padx=1, pady=1)
Blockchain_btn = tk.Button(left_frame, text='Blockchain', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
Blockchain_btn.grid(row=4, column=0, padx=1, pady=1)
Trx_btn = tk.Button(left_frame, text='Transaction', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
Trx_btn.grid(row=5, column=0, padx=1, pady=1)
Verify_btn = tk.Button(left_frame, text='Verifying', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
Verify_btn.grid(row=6, column=0, padx=1, pady=1)
Explorer_btn = tk.Button(left_frame, text='Explorer', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
Explorer_btn.grid(row=7, column=0, padx=1, pady=1)
AboutUs_btn = tk.Button(left_frame, text='About Us', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
AboutUs_btn.grid(row=8, column=0, padx=1, pady=1)
Exit_btn = tk.Button(left_frame, text='Exit', height=1, width=9, bg='#3c3c3c', fg='white', font='Arial, 24');
Exit_btn.grid(row=9, column=0, padx=1, pady=1)
tk.Label(left_frame, text=' ', height=2, width=9, bg='gray', fg='white').grid(row=10, column=0, padx=1, pady=1)
# endregion

def On_text_change(evevt):
    text = Sha_text.get('1.0', 'end').strip()
    text = text.replace("\n", "\\n")
    texth = hashlib.sha256(text.encode())
    Hash = texth.hexdigest()
    Sha_hash_lbl.config(text=Hash)


def Hash_page():
    global Sha_text, Sha_hash_lbl

    # right_frame.destroy()
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)
    # Widgets in Right Frame
    SHA = tk.Label(right_frame, text='SHA256 Hash', bg='#3c3c3c', fg='white', font=(fonts[0], 30, 'bold'))
    SHA.grid(row=0, column=0);
    SHA.place(x=50, y=30);

    # Text_Box for Data
    Sha_text = tk.Text(right_frame, height=15, width=66, bg='#e0e0e0', borderwidth=2, relief="ridge", \
                       font=('Arial', 18));
    Sha_text.grid(row=1, column=0);
    Sha_text.place(x=50, y=90);

    # Key Event in Text Box
    Sha_text.bind('<KeyRelease>', On_text_change)

    Sha_hash = tk.Label(right_frame, text='Hash: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Sha_hash.grid(row=2, column=0);
    Sha_hash.place(x=48, y=535)
    # Data Hash
    Sha_hash_lbl = tk.Label(right_frame, text='Display Hash here', bg='#3c3c3c', fg='white', \
                            font=("Arial Bold", 16), borderwidth=3, relief='sunken', height=2, width=60)
    Sha_hash_lbl.grid(row=2, column=1);
    Sha_hash_lbl.place(x=128, y=529)

def Block_hash_Cal(Bnt, Ent, Txtbox, prv,  Hash, event=None):
    ent = Ent.get().strip()
    txtbox = Txtbox.get('1.0', 'end').strip()
    txtbox = txtbox.replace("\n", "\\n")
    Blkdata = Bnt + ent + txtbox + prv
    texth = hashlib.sha256(Blkdata.encode())
    Hashval = texth.hexdigest()
    Hash.config(text=Hashval)

def Confirm(nBlock):
    #print('In Conf Func\n')
    msg = Msg.askyesno('Confirmation', 'Do you want to add this Block in Blockchain.!')
    print(msg); global PageNo, gldata
    if msg :
        MyBC.Add_block(nBlock)
        PageNo = MyBC.get_ind()-1
        gldata = ''
        Block_Page()
    else:
        print('Block is not added to Blockchain.')

def Block_Page():
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlock = tk.Label(right_frame, text='Full Block Mining', bg='#3c3c3c', fg='white', font=(fonts[0], 30, "bold"))
    FulBlock.grid(row=0, column=0);
    FulBlock.place(x=50, y=30);

    # Block Frame
    block_frame = tk.Frame(right_frame, width=870, height=450, bg='#808080')
    block_frame.grid(row=0, column=1, padx=2, pady=2)
    block_frame.place(x=44, y=90)
    block_frame.grid_propagate(False)

    # Block No Label
    BlkNo = tk.Label(right_frame, text='Block No: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    BlkNo.grid(row=2, column=0);
    BlkNo.place(x=50, y=95)
    # Show Block No. #
    BlkNo_lbl = tk.Label(right_frame, text='  '+str(MyBC.get_ind()), anchor='w', bg='#3c3c3c', fg='white', \
                            font=("Arial Bold", 20), borderwidth=2, relief='sunken', height=1, width=15)
    BlkNo_lbl.grid(row=2, column=1);
    BlkNo_lbl.place(x=196, y=95)

    # Nonce Label
    Nonce_lbl = tk.Label(right_frame, text='Nonce : ', bg='#3c3c3c', fg='white', font=("Arial Bold", 19))
    Nonce_lbl.grid(row=2, column=0);
    Nonce_lbl.place(x=500, y=95)
    # Nonce Entry
    Nonce_ent = tk.Entry(right_frame, bg='#3c3c3c', width=18, fg='white', font=("Arial", 21))
    Nonce_ent.grid(row=2, column=0);
    Nonce_ent.place(x=605, y=95)

    # TimeStamp Label
    TmStp = tk.Label(right_frame, text='TimeStamp: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    TmStp.grid(row=2, column=0);
    TmStp.place(x=50, y=145)
    Bn = str(MyBC.get_ind())
    t = str(dt.datetime.now())
    Bnt =Bn + t
    # Timestamp DateTime
    TmStp_lbl = tk.Label(right_frame, text=dt.datetime.now().strftime("Time : %H:%M:%S          Date : %d - %m - %Y"), \
                    anchor='center', bg='#3c3c3c', fg='white', \
                        font=("Arial Bold", 20), borderwidth=2, relief='sunken', height=1, width=39)
    TmStp_lbl.grid(row=2, column=1);
    TmStp_lbl.place(x=228, y=145)

    # Data Text Box Label
    Data_lbl = tk.Label(right_frame, text='Data: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Data_lbl.grid(row=2, column=0);
    Data_lbl.place(x=50, y=195)

    Data_TextBox = tk.Text(right_frame,width=58, height=10, bg='#3c3c3c', fg='white', font=("Arial", 18))
    Data_TextBox.grid(row=2, column=0);
    Data_TextBox.place(x=138, y=195)

    # Preveous Hash Label
    PrH = MyBC.get_last_block().Hash
    Pre_hash = tk.Label(right_frame, text='P_H:', width=4, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Pre_hash.grid(row=2, column=0);
    Pre_hash.place(x=50, y=485)
    # Timestamp DateTime
    Pre_hash_lbl = tk.Label(right_frame, text=PrH, anchor='center', bg='#3c3c3c', fg='white', \
                            font=("Arial Bold", 16), borderwidth=2, relief='sunken', height=2, width=60)
    Pre_hash_lbl.grid(row=2, column=1);
    Pre_hash_lbl.place(x=128, y=479)

    Block_hash = tk.Label(right_frame, text='Hash: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Block_hash.grid(row=2, column=0);
    Block_hash.place(x=45, y=557)
    # Data Hash
    Block_hash_lbl = tk.Label(right_frame, text='0'*64, bg='#606060', fg='white', \
                            font=("Arial Bold", 16), borderwidth=3, relief='sunken', height=2, width=60)
    Block_hash_lbl.grid(row=2, column=1);
    Block_hash_lbl.place(x=128, y=550)
    Nonce_ent.bind("<KeyRelease>", lambda event: Block_hash_Cal(Bnt, Nonce_ent, Data_TextBox,PrH,Block_hash_lbl, event))
    Data_TextBox.bind("<KeyRelease>", lambda event: Block_hash_Cal(Bnt, Nonce_ent, Data_TextBox,PrH,Block_hash_lbl, event))
    global gldata
    Mine_btn = tk.Button(right_frame, text='Mine', height=1, width=9, bg='#3c3c3c', fg='white', \
                          font='Arial, 24', command=lambda: Confirm(BC.Block(str(MyBC.get_ind()), Nonce_ent.get().strip(),\
                        str(dt.datetime.now()), PrH, Data_TextBox.get('1.0', 'end').strip().replace("\n", "\\n") + gldata)))
    Mine_btn.grid(row=3, column=0, padx=1, pady=1)
    Mine_btn.place(x=735, y=615)

def Go_Prev():
    global PageNo, PreP, NxtP
    print('PageNo Value Go_Pre1: ', PageNo)
    PageNo = PageNo - 1
    print('PageNo Value Go_Pre2: ', PageNo)
    PreP = MyBC.find_block(PageNo - 1)
    if PreP == 'BlockNotFound':
        PageNo = PageNo + 1
    print('PageNo Value Go_Pre3: ', PageNo)
    NxtP = MyBC.find_block(PageNo)
    PreP = MyBC.find_block(PageNo - 1)
    Blockchain_Page()

def Go_Next():
    global PageNo, PreP, NxtP
    print('PageNo Value Go_Nxt1: ', PageNo)
    PageNo = PageNo + 1
    print('PageNo Value Go_Nxt2: ', PageNo)
    NxtP = MyBC.find_block(PageNo)
    print('Value of NxtP', NxtP)
    if NxtP == 'BlockNotFound':
        PageNo = PageNo - 1
    print('PageNo Value Go_Nxt3: ', PageNo)
    PreP = MyBC.find_block(PageNo - 1)
    NxtP = MyBC.find_block(PageNo)
    Blockchain_Page()

# Blockchain Page
def Blockchain_Page():
    # =========Frames Initaialization========
    # region
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlockchain = tk.Label(right_frame, text='Blockchain', bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    FulBlockchain.grid(row=0, column=0);
    FulBlockchain.place(x=50, y=30);

    # Block1 Frame
    block1_frame = tk.Frame(right_frame, width=620, height=450, bg='#808080')
    block1_frame.grid(row=0, column=1, padx=2, pady=2)
    block1_frame.place(x=44, y=90)
    block1_frame.grid_propagate(False)
    # Block2 Frame
    block2_frame = tk.Frame(right_frame, width=620, height=450, bg='#808080')
    block2_frame.grid(row=0, column=1, padx=2, pady=2)
    block2_frame.place(x=700, y=90)
    block2_frame.grid_propagate(False)
    # endregion
    global PageNo, PreP, NxtP
    print('PageNo Value BlkPage1: ', PageNo)
    #PageNo = MyBC.get_ind()-1
    NxtP = MyBC.find_block(PageNo)
    PreP = MyBC.find_block(PageNo - 1)

    # =========Block No 2=========
    # region Not working
    # Block No Label
    BlkNo = tk.Label(right_frame, text='Block No: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    BlkNo.grid(row=2, column=0);
    BlkNo.place(x=50, y=105)
    # Show Block No. #
    BlkNo_lbl = tk.Label(right_frame, text=str(PreP.index), bg='#3c3c3c', fg='white', \
                         font=("Arial Bold", 15), borderwidth=2, relief='sunken', height=1, width=14)
    BlkNo_lbl.grid(row=2, column=1);
    BlkNo_lbl.place(x=157, y=105)

    # Nonce Label
    Nonce_lbl = tk.Label(right_frame, text='Nonce : ', bg='#3c3c3c', fg='white', font=("Arial Bold", 14))
    Nonce_lbl.grid(row=2, column=0);
    Nonce_lbl.place(x=350, y=105)
    # Nonce Entry
    BpNonce_lbl = tk.Label(right_frame, text=str(PreP.nonce), bg='#3c3c3c', width=19, fg='white', font=("Arial", 15))
    BpNonce_lbl.grid(row=2, column=0);
    BpNonce_lbl.place(x=435, y=105)

    # TimeStamp Label
    TmStp = tk.Label(right_frame, text='TimeStamp: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    TmStp.grid(row=2, column=0);
    TmStp.place(x=50, y=148)

    # Timestamp DateTime
    TmStp_lbl = tk.Label(right_frame, text=str(PreP.timstp), anchor='center', bg='#3c3c3c', fg='white', \
                         font=("Arial Bold", 15), borderwidth=2, relief='sunken', height=1, width=39)
    TmStp_lbl.grid(row=2, column=1);
    TmStp_lbl.place(x=180, y=148)

    # Data Text Box Label
    Data_lbl = tk.Label(right_frame, text='Data: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Data_lbl.grid(row=2, column=0);
    Data_lbl.place(x=50, y=195)

    Data_Box1_lbl = tk.Text(right_frame, wrap="word", width=59, height=15, bg='#3c3c3c', fg='white', font=("Arial", 13))
    Data_Box1_lbl.insert(tk.END, str(PreP.data))
    Data_Box1_lbl.grid(row=0, column=0)
    Data_Box1_lbl.place(x=117, y=195)
    scrollbar1 = tk.Scrollbar(right_frame, command=Data_Box1_lbl.yview)
    scrollbar1.grid(row=0, column=1, sticky="ns")
    Data_Box1_lbl.config(yscrollcommand=scrollbar1.set)

    # Preveous Hash Label
    Pre_hash = tk.Label(right_frame, text='P_H: ', width=4, bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Pre_hash.grid(row=2, column=0);
    Pre_hash.place(x=50, y=495)
    # Timestamp DateTime
    Pre_hash_lbl = tk.Label(right_frame, text=str(PreP.PrevH), anchor='center', bg='#3c3c3c', fg='white', \
                            font=("Arial Bold", 11), borderwidth=2, relief='sunken', height=2, width=59)
    Pre_hash_lbl.grid(row=2, column=1);
    Pre_hash_lbl.place(x=115, y=490)

    Block_hash = tk.Label(right_frame, text='Hash: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Block_hash.grid(row=2, column=0);
    Block_hash.place(x=45, y=557)
    # Data Hash
    Block_hash_lbl = tk.Label(right_frame, text=str(PreP.Hash), bg='#606060', fg='white', \
                              font=("Arial Bold", 11), borderwidth=3, relief='sunken', height=2, width=60)
    Block_hash_lbl.grid(row=2, column=1);
    Block_hash_lbl.place(x=115, y=550)
    # endregion

    PreBlk_btn = tk.Button(right_frame, text='Previous Blocks', height=1, width=13, bg='#3c3c3c', fg='white', \
                         font='Arial, 19', command=Go_Prev)
    PreBlk_btn.grid(row=3, column=0, padx=1, pady=1)
    PreBlk_btn.place(x=45, y=615)

    # =========Block No 2=========
    # region
    # Block No Label
    BlkNo1 = tk.Label(right_frame, text='Block No: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    BlkNo1.grid(row=2, column=0);
    BlkNo1.place(x=706, y=105)
    # Show Block No. #
    BlkNo1_lbl = tk.Label(right_frame, text=str(NxtP.index), bg='#3c3c3c', fg='white', \
                         font=("Arial Bold", 15), borderwidth=2, relief='sunken', height=1, width=14)
    BlkNo1_lbl.grid(row=2, column=1);
    BlkNo1_lbl.place(x=157+656, y=105)

    # Nonce Label
    Nonce1_lbl = tk.Label(right_frame, text='Nonce : ', bg='#3c3c3c', fg='white', font=("Arial Bold", 14))
    Nonce1_lbl.grid(row=2, column=0);
    Nonce1_lbl.place(x=350+656, y=105)
    # Nonce Entry
    Nonce1_lbl = tk.Label(right_frame, text=str(NxtP.nonce), bg='#3c3c3c', width=19, fg='white', font=("Arial", 15))
    Nonce1_lbl.grid(row=2, column=0);
    Nonce1_lbl.place(x=435+656, y=105)

    # TimeStamp Label
    TmStp1 = tk.Label(right_frame, text='TimeStamp: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    TmStp1.grid(row=2, column=0);
    TmStp1.place(x=706, y=148)

    # Timestamp DateTime
    TmStp1_lbl = tk.Label(right_frame, text=str(NxtP.timstp), anchor='center', bg='#3c3c3c', fg='white', \
                         font=("Arial Bold", 15), borderwidth=2, relief='sunken', height=1, width=39)
    TmStp1_lbl.grid(row=2, column=1);
    TmStp1_lbl.place(x=180+656, y=148)

    # Data Text Box Label
    Data1_lbl = tk.Label(right_frame, text='Data: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Data1_lbl.grid(row=2, column=0);
    Data1_lbl.place(x=706, y=195)

    Data_Box2_lbl = tk.Text(right_frame, wrap="word", width=59, height=15, bg='#3c3c3c', fg='white', font=("Arial", 13))
    Data_Box2_lbl.insert(tk.END, str(NxtP.data))
    Data_Box2_lbl.grid(row=0, column=0)
    Data_Box2_lbl.place(x=117+656, y=195)
    scrollbar = tk.Scrollbar(right_frame, command=Data_Box2_lbl.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    Data_Box2_lbl.config(yscrollcommand=scrollbar.set)

    # Preveous Hash Label
    Pre_hash1 = tk.Label(right_frame, text='P_H ', width=4, bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Pre_hash1.grid(row=2, column=0);
    Pre_hash1.place(x=706, y=495)
    # Timestamp DateTime
    Pre_hash1_lbl = tk.Label(right_frame, text=str(NxtP.PrevH), anchor='center', bg='#3c3c3c', fg='white', \
                            font=("Arial Bold", 11), borderwidth=2, relief='sunken', height=2, width=59)
    Pre_hash1_lbl.grid(row=2, column=1);
    Pre_hash1_lbl.place(x=115+656, y=490)

    Block_hash1 = tk.Label(right_frame, text='Hash: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 15))
    Block_hash1.grid(row=2, column=0);
    Block_hash1.place(x=701, y=557)
    # Data Hash
    Block_hash1_lbl = tk.Label(right_frame, text=str(NxtP.Hash), bg='#606060', fg='white', \
                              font=("Arial Bold", 11), borderwidth=3, relief='sunken', height=2, width=60)
    Block_hash1_lbl.grid(row=2, column=1);
    Block_hash1_lbl.place(x=115+656, y=550)

    NxtBlk_btn = tk.Button(right_frame, text='Next Blocks', height=1, width=13, bg='#3c3c3c', fg='white', \
                         font='Arial, 19', command=Go_Next)
    NxtBlk_btn.grid(row=3, column=0, padx=1, pady=1)
    NxtBlk_btn.place(x=1115, y=615)
    # endregion

def Transfer(frm, to, coin, tmst):
    global gldata
    frm = ' <From> ' + frm
    to = ' <To> '+ to
    coin = ' <Coins> '+ coin
    tmst = ' <Tmstp> '+ tmst
    gldata = gldata + frm + to + coin + tmst

# Transaction Page
def Transaction_Page():
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlock = tk.Label(right_frame, text='Transaction', bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    FulBlock.grid(row=0, column=0);
    FulBlock.place(x=150, y=30);


    # Block Frame
    block_frame = tk.Frame(right_frame, width=770, height=450, bg='#808080')
    block_frame.grid(row=0, column=1, padx=2, pady=2)
    block_frame.place(x=150, y=90)
    block_frame.grid_propagate(False)

    # Full Block Label
    TpSc_lbl = tk.Label(right_frame, text='Send Coins',width=11, bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    TpSc_lbl.grid(row=0, column=0);
    TpSc_lbl.place(x=260, y=110);

    # Nonce Label
    From_lbl = tk.Label(right_frame, text=' From : ',width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    From_lbl.grid(row=2, column=0);
    From_lbl.place(x=260, y=190)
    # Nonce Entry
    From_ent = tk.Entry(right_frame, text='From :  ', bg='#3c3c3c', width=18, fg='white', font=("Arial", 23))
    From_ent.grid(row=2, column=0);
    From_ent.place(x=380, y=190)
    # Nonce Label
    To_lbl = tk.Label(right_frame, text='   To   : ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    To_lbl.grid(row=2, column=0);
    To_lbl.place(x=260, y=260)
    # Nonce Entry
    To_ent = tk.Entry(right_frame, text='To :  ', bg='#3c3c3c', width=18, fg='white', font=("Arial", 23))
    To_ent.grid(row=2, column=0);
    To_ent.place(x=380, y=260)

    # Nonce Label
    Coins_lbl = tk.Label(right_frame, text='Coins : ',width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Coins_lbl.grid(row=2, column=0);
    Coins_lbl.place(x=260, y=330)
    # Nonce Entry
    Coins_ent = tk.Entry(right_frame, text='Coins :  ', bg='#3c3c3c', width=18, fg='white', font=("Arial", 23))
    Coins_ent.grid(row=2, column=0);
    Coins_ent.place(x=380, y=330)

    # Nonce Label
    Tstp_lbl = tk.Label(right_frame, text='Tstmp: ',width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Tstp_lbl.grid(row=2, column=0);
    Tstp_lbl.place(x=260, y=400)
    # Nonce Entry
    Tstmp_lbl = tk.Label(right_frame, text=str(dt.datetime.now()), bg='#3c3c3c', width=20, fg='white', font=("Arial Bold", 18))
    Tstmp_lbl.grid(row=2, column=0);
    Tstmp_lbl.place(x=380, y=400)


    Trx_hash = tk.Label(right_frame, text='Trx ID: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Trx_hash.grid(row=2, column=0);
    Trx_hash.place(x=150, y=557)
    # Data Hash
    Trx_hash_lbl = tk.Label(right_frame, text='24856fddbbd554c6336c7e5e313a86a61a062946b41c66b5991fb', bg='#3c3c3c', fg='white', \
                              font=("Arial Bold", 16), borderwidth=3, relief='sunken', height=2, width=51)
    Trx_hash_lbl.grid(row=2, column=1);
    Trx_hash_lbl.place(x=250, y=550)

    Transfer_btn = tk.Button(right_frame, text='Transfer', height=1, width=9, bg='#3c3c3c', fg='white', \
                         font='Arial, 24', command= lambda : Transfer(From_ent.get().strip(), To_ent.get().strip(),\
                             Coins_ent.get().strip(), str(dt.datetime.now())))
    Transfer_btn.grid(row=3, column=0, padx=1, pady=1)
    Transfer_btn.place(x=740, y=615)

Block_hash_lbl = ''
def Verify():
    global Block_hash_lbl
    Ver = MyBC.is_valid_chain()
    if Ver:
        Block_hash_lbl.config(text='Blockchain is Verified')
    else:
        Block_hash_lbl.config(text='Blockchain is Not Verified')
def Verify_Page():
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlock = tk.Label(right_frame, text='Verify Blocks', bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    FulBlock.grid(row=0, column=0);
    FulBlock.place(x=50, y=30);

    # Block Frame
    block_frame = tk.Frame(right_frame, width=870, height=450, bg='#808080')
    block_frame.grid(row=0, column=1, padx=2, pady=2)
    block_frame.place(x=44, y=90)
    block_frame.grid_propagate(False)

    global Block_hash_lbl
    # Data Hash
    Block_hash_lbl = tk.Label(right_frame, text='Verification procces', bg='#606060', fg='white', \
                            font=("Arial Bold", 16), borderwidth=3, relief='sunken', height=2, width=60)
    Block_hash_lbl.grid(row=2, column=1);
    Block_hash_lbl.place(x=90, y=250)

    Verify_btn = tk.Button(right_frame, text='Verify', height=1, width=9, bg='#3c3c3c', fg='white', \
                          font='Arial, 24', command=Verify)
    Verify_btn.grid(row=3, column=0, padx=1, pady=1)
    Verify_btn.place(x=700, y=350)

def Explor_Page():
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlock = tk.Label(right_frame, text='Explor Transaction', bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    FulBlock.grid(row=0, column=0);
    FulBlock.place(x=150, y=30);

    # Block Frame
    block_frame = tk.Frame(right_frame, width=770, height=450, bg='#808080')
    block_frame.grid(row=0, column=1, padx=2, pady=2)
    block_frame.place(x=150, y=155)
    block_frame.grid_propagate(False)

    # Nonce Label
    Blk_lbl = tk.Label(right_frame, text='BlkNo: ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Blk_lbl.grid(row=2, column=0);
    Blk_lbl.place(x=260, y=190)
    # Nonce Entry
    BlkNo_lbl = tk.Label(right_frame, text=' ####### ', bg='#3c3c3c', width=18, fg='white',
                         font=("Arial Bold", 20))
    BlkNo_lbl.grid(row=2, column=0);
    BlkNo_lbl.place(x=380, y=190)
    # Nonce Label
    From_lbl = tk.Label(right_frame, text=' From : ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    From_lbl.grid(row=2, column=0);
    From_lbl.place(x=260, y=260)
    # Nonce Entry
    From_Coin_lbl = tk.Label(right_frame, text=' ####### ', bg='#3c3c3c', width=18, fg='white',
                         font=("Arial Bold", 20))
    From_Coin_lbl.grid(row=2, column=0);
    From_Coin_lbl.place(x=380, y=260)

    # Nonce Label
    To_lbl = tk.Label(right_frame, text='   To   : ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    To_lbl.grid(row=2, column=0);
    To_lbl.place(x=260, y=330)
    # Nonce Entry
    To_Coin_lbl = tk.Label(right_frame, text=' ####### ', bg='#3c3c3c', width=18, fg='white',
                         font=("Arial Bold", 20))
    To_Coin_lbl.grid(row=2, column=0);
    To_Coin_lbl.place(x=380, y=330)

    # Nonce Label
    Tstp_lbl = tk.Label(right_frame, text='Coins : ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Tstp_lbl.grid(row=2, column=0);
    Tstp_lbl.place(x=260, y=400)
    # Nonce Entry
    Tstmp_lbl = tk.Label(right_frame, text=' ####### ', bg='#3c3c3c', width=18, fg='white',
                         font=("Arial Bold", 20))
    Tstmp_lbl.grid(row=2, column=0);
    Tstmp_lbl.place(x=380, y=400)

    Tstp_lbl = tk.Label(right_frame, text='Tstmp: ', width=6, bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Tstp_lbl.grid(row=2, column=0);
    Tstp_lbl.place(x=260, y=470)
    # Nonce Entry
    Tstmp_lbl = tk.Label(right_frame, text=' Transfer DateTime ', bg='#3c3c3c', width=18, fg='white',
                         font=("Arial Bold", 20))
    Tstmp_lbl.grid(row=2, column=0);
    Tstmp_lbl.place(x=380, y=470)

    '''# TimeStamp Label
    TmStp = tk.Label(right_frame, text='TimeStamp:', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    TmStp.grid(row=2, column=0);
    TmStp.place(x=195, y=370)
    '''

    Trx_hash = tk.Label(right_frame, text='Trx ID: ', bg='#3c3c3c', fg='white', font=("Arial Bold", 20))
    Trx_hash.grid(row=2, column=0);
    Trx_hash.place(x=150, y=100)
    # Data Hash
    Trx_hash_ent = tk.Entry(right_frame, text='Display Hash here', bg='#3c3c3c', fg='white', \
                            font=("Arial", 23), borderwidth=3, relief='sunken', width=39)
    Trx_hash_ent.grid(row=2, column=1);
    Trx_hash_ent.place(x=250, y=95)

    Transfer_btn = tk.Button(right_frame, text='Search', height=1, width=9, bg='#3c3c3c', fg='white', \
                             font='Arial, 24')
    Transfer_btn.grid(row=3, column=0, padx=1, pady=1)
    Transfer_btn.place(x=740, y=615)

def AboutUs_Page():
    # Initialize Right Frame
    right_frame = tk.Frame(window, width=1350, height=700, bg='#3c3c3c')
    right_frame.grid(row=0, column=1, padx=5, pady=5)
    right_frame.grid_propagate(False)

    # Full Block Label
    FulBlock = tk.Label(right_frame, text='About Us', bg='#3c3c3c', fg='white', font=("Arial Bold", 30))
    FulBlock.grid(row=0, column=0);
    FulBlock.place(x=50, y=30);

    # Farooq Frame
    Far_frame = tk.Frame(right_frame, width=400, height=450, bg='#808080')
    Far_frame.grid(row=0, column=1, padx=2, pady=2)
    Far_frame.place(x=50, y=140)
    Far_frame.grid_propagate(False)

    # Muhammad Farooq
    Far_lbl = tk.Label(right_frame, text='Muhammad Farooq 19064 ', fg='black', font=("Arial Bold", 20))
    Far_lbl.grid(row=2, column=0);
    Far_lbl.place(x=70, y=180)


    # Zaheer Abbas
    Zar_lbl = tk.Label(right_frame, text='Zaheer Abbas 19064 ', fg='black', font=("Arial Bold", 20))
    Zar_lbl.grid(row=2, column=0);
    Zar_lbl.place(x=70, y=260)

    # Zaheer Ali
    ZarA_lbl = tk.Label(right_frame, text='Zaheer Ali 19064 ', fg='black', font=("Arial Bold", 20))
    ZarA_lbl.grid(row=2, column=0);
    ZarA_lbl.place(x=70, y=340)

    # Hashim  Khalid
    Has_lbl = tk.Label(right_frame, text='Hasham Khalid', fg='black', font=("Arial Bold", 20))
    Has_lbl.grid(row=2, column=0);
    Has_lbl.place(x=70, y=420)

    # Class BSCS 5th
    Cls_lbl = tk.Label(right_frame, text='Class BSCS 5th', width=21, fg='black', font=("Arial Bold", 20))
    Cls_lbl.grid(row=2, column=0);
    Cls_lbl.place(x=70, y=520)


    # Z Abbas Frame
    Zar_frame = tk.Frame(right_frame, width=820, height=450, bg='#808080')
    Zar_frame.grid(row=0, column=1, padx=2, pady=2)
    Zar_frame.place(x=475, y=140)
    Zar_frame.grid_propagate(False)

    About_Us = '''We are software developer and Researcher. We are trying  
to solve some major real life Problem by using Blockchain 
Technology. In this Project we simply Explain that. What
is Blockchain and who it works.
Blockchain is a decentralized digital ledger that securely
records transactions. It uses cryptographic algorithms for
transparency and immutability. Beyond cryptocurrencies,
blockchain has applications in supply chain management, 
healthcare, finance, and more, offering enhanced security
and efficiency. Its decentralized nature eliminates the 
need for a central authority, promoting trust among 
participants.'''

    # About Paragraph
    Abo_lbl = tk.Label(right_frame, text=About_Us, fg='black', font=("Arial Bold", 20))
    Abo_lbl.grid(row=2, column=0);
    Abo_lbl.place(x=500, y=180)

# ===========Page Functions Call=========
# Display Hash Page
# region

def Show_hash_page():
    Hash_page()

def Show_block_page():
    Block_Page()

def Show_Trx_Page():
    Transaction_Page()

def Show_Verify_Page():
    Verify_Page()

def Show_Explor_Page():
    Explor_Page()

def Show_AboutUs_Page():
    AboutUs_Page()

def Exit_Win():
    window.destroy()

Show_hash_page()
# Buttons Config
Hash_btn.config(command=Show_hash_page)
Block_btn.config(command=Show_block_page)
Blockchain_btn.config(command=Blockchain_Page)
Trx_btn.config(command=Show_Trx_Page)
Verify_btn.config(command=Show_Verify_Page)
Explorer_btn.config(command=Show_Explor_Page)
AboutUs_btn.config(command=Show_AboutUs_Page)
Exit_btn.config(command=Exit_Win)

# endregion

window.mainloop()
