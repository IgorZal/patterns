class Header:
    
    def add_header(self,txt):
        txt[0]="<h1>"+txt[0]+"</h1>"
        return txt

        
class Paragraph:
    
    def add_paragraphs(self,txt):
        txt=''.join(txt)
        txt=txt.split('   ')
        for i in range(1, len(txt)):
            txt[i]="<p>"+txt[i]+"</p>"
        return txt
    

class Body():
    
    def add_start_end(self,txt):
        txt.insert(0,'<body>')
        txt.insert(len(txt),'</body>')
        return txt


class Translator():
    def __init__(self):
        self.body=Body()
        self.header=Header()
        self.paragraph=Paragraph()
        self.text=None

    def add_text(self,txt):
        self.text=txt.split('.')

    def translate(self):
        
        self.text=self.header.add_header(self.text)
        self.text=self.paragraph.add_paragraphs(self.text)
        self.text=self.body.add_start_end(self.text)

        for tags in self.text:
            print(tags)


a="The Grand Canyon.   The Grand Canyon\
is 277 miles long, up to 18 miles\
wide and attains a depth of over a mile.   \
For thousands of years, the area has been \
inhabited by Native Americans,\
who built settlements within the canyon and its many caves"

i=Translator()
i.add_text(a)
i.translate()



