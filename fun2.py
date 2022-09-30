def marks(**data):
    with open('marks.text','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}\n')
marks(rajesj=200,brjesh=58)
marks(aman=200)
marks()



