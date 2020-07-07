
#输出器
class htmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data == None:
            return
        self.datas.append(data)

    def output_html(self):
        #表格
        fout = open("output.html","w")

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            #python 默认编码 ASCII；
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td>%s</td>" % data["title"])
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</html>")
        fout.write("</body>")