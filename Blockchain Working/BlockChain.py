# M Farooq BSCS 5th 19064
# BlockChain Development
import hashlib
import datetime as dt
import random as rand

def Write_Block(BlkNo, Nonce, Timstp, PrevH, Data):
    Wrt_Block = open('Blockchain.txt', 'a')
    B_No = '<BlkNo> ' + BlkNo
    Non  = ' <Nonce> '+ Nonce
    Tms = ' <Tstp> ' + Timstp
    PreH = ' <PrevH> ' + PrevH
   # Has = ' <Hash> ' + Hash
    Dt = ' <Data> ' + Data + ' <End>'
    Wrt_Block.write(B_No + Non + Tms + PreH + Dt + '\n')
    Wrt_Block.close()

def Data_Org(Block):

    # Extracting the values using string manipulation
    blk_no = int(Block.split("<BlkNo>")[1].split("<")[0].strip())
    nonce = int(Block.split("<Nonce>")[1].split("<")[0].strip())
    timestamp = Block.split("<Tstp>")[1].split("<")[0].strip()
    prev_hash = Block.split("<PrevH>")[1].split("<")[0].strip()
    #hash_val = Block.split("<Hash>")[1].split("<")[0].strip()
    data = Block.split("<Data>")[1].split("<End>")[0].strip()

    # Creating the list with the extracted values
    data_list = [blk_no, nonce, timestamp, prev_hash, data]

    return data_list

def Read_Block(BlkNo):
    Red_Block = open('Blockchain.txt', 'r')
    Blocks = Red_Block.readlines()
    if BlkNo < len(Blocks):
        BlockLine = Blocks[BlkNo]

        data_list = Data_Org(BlockLine)
        Red_Block.close()
        #print(data_list)
        return data_list
    else:
        Red_Block.close()
        return 'BlockNotFound'


#Data__ = Read_Block(1)
#print(Data__)
def get_hash(data):
    Hash = hashlib.sha256(data.encode())
    return Hash.hexdigest()

class Block:
    def __init__(self, index, Nonc, timstp, PrevH, data):
        self.index = index
        self.timstp = timstp
        self.data = data
        self.PrevH = PrevH
        self.nonce = Nonc #rand.randint(100000000, 10000000000)
        self.Hash = self.get_hash()

    def get_hash(self):
        Aldata = str(self.index) + str(self.timstp) + str(self.data) + str(self.PrevH) + str(self.nonce)
        Hash = hashlib.sha256(Aldata.encode())
        return Hash.hexdigest()        


class Blockchain:
    def __init__(self):
        self.Chain = []
        Rd_block = open('Blockchain.txt', 'r')
        for line in Rd_block:
            dl = Data_Org(line)
            print(dl)
            _Block = Block(dl[0], dl[1], dl[2], dl[3], dl[4])
            self.Chain.append(_Block)

        Rd_block.close()
        #self.gen_Block()

    def gen_Block(self):
        gen_block = Block(0, rand.randint(100000000, 10000000000), dt.datetime.now(), '0'*64, 'This is Genesis Block')
        self.Chain.append(gen_block)

    def get_last_block(self):
        return self.Chain[-1]

    def get_ind(self):
        return len(self.Chain)

    def Add_block(self, nblk):
        nblk.PrevH = self.get_last_block().Hash
        nblk.Hash = nblk.get_hash()
        self.Chain.append(nblk)
        Write_Block(nblk.index, nblk.nonce, nblk.timstp, nblk.PrevH, nblk.data)

    def find_block(self, N):
        if 0 <= N < self.get_ind():
            return self.Chain[N]
        else:
            return 'BlockNotFound'

    def is_valid_chain(self):
        for i in range(1, len(self.Chain)):
            Crt_block = self.Chain[i]
            Prev_block = self.Chain[i-1]
            if Crt_block.Hash != Crt_block.get_hash():
                return False
            if Crt_block.PrevH != Prev_block.Hash:
                return False

        return True

# Create Object For Blockchain
# MyBC = Blockchain()
# print(len(MyBC.Chain))
'''
# Create Object For Blockchain
# MyBC = Blockchain()
# print(len(MyBC.Chain))

# 2nd and 3rd Block data
 2nd and 3rd Block data
Data = "Get Data to Store in Blockchain"
Block1 = Block(MyBC.get_ind() , dt.datetime.now(), Data)
MyBC.Add_block(Block1)
#print(Block1.data)
Data = "Get Data to Store in 2nd Block"
Block2 = Block(len(MyBC.Chain) , dt.datetime.now(), Data)
MyBC.Add_block(Block2)
#print(Block2.data)
Range = MyBC.get_ind()
#print(MyBC.get_ind())

Range = MyBC.get_ind()
for i in range(Range):
    Bd = MyBC.Chain[i]
    print('Block Index   : ', Bd.index)
    print('Time Stamp  : ',Bd.timstp)
    print('Block Data     : ',  Bd.data)
    print('PrevHash       : ',  Bd.PrevH)
    print('Nonce Value : ', Bd.nonce)
    print('Current Hash : ', Bd.Hash)
    print()

print(MyBC.is_valid_chain())
    
    
#HashCh = get_hash('')
#print(HashCh)
#print (dt.datetime.now())
'''