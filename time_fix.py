import sys

def main():
    if len(sys.argv) < 1:
        print('인자를 입력해주세요.')
        return
    
    data_path = sys.argv[1]
    
    with open(data_path, "r") as src:
        while(True):
            source_path = src.readline()
            if not source_path : break
            text_path = source_path.split(',')[1].strip()
            arr = []
            with open('./data/'+text_path+".txt", "r") as r:
                while(True):
                    temp = r.readline()
                    if not temp: break
                    temp = temp.split(',')
                    print(temp)
                    temp[2] = '%d:%d:%d' % (int(temp[0]) // 29.97 // 3600, int(temp[0])//29.97%3600//60, int(temp[0])//29.97%60)
                    temp[3] = '%d:%d:%d' % (int(temp[1]) // 29.97 // 3600, int(temp[1])//29.97%3600//60 , int(temp[1])//29.97%60)
                    arr.append(temp)
                    print(temp)
            with open('./data/'+text_path+".txt", "w") as w:
                for i in arr:
                    w.write(i[0]+","+i[1]+", "+i[2]+","+i[3]+"\n")

        
if __name__ == "__main__":
    main()
