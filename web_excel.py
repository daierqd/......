import web
import html
import seek_similarity
import os_excel
import re

urls = (
    '/password','password',
    '/delete','delete',
    '/home','home',
    '/add','add',
    '/jur','jur',
    '/jurs','jurs',
    '/result=/\d+','result',
    '/lock/\d+','lock',
    )

render = web.template.render("resources_get")

class password:
    def GET(self):
        return open('password.html',encoding='utf-8').read()

class add:
    def POST(self):
        data = web.input()
        k = dict(data)
        title = k['question']
        counts = k['count']
        names = html.unescape(title)
        countss = html.unescape(counts)
        os_excel.add(names,countss)
        return open('add.html',encoding='utf-8').read()

class delete:
    def POST(self):
        data = web.input()
        k = dict(data)
        number = int(k['question'])
        l = os_excel.duiying(number)
        os_excel.delete(l)
        return open('delete.html',encoding='utf-8').read()


class lock:
    def GET(self):
        aa = []
        a = web.ctx.env
        members = a['PATH_INFO']
        member = members.strip('/lock/')
        title = os_excel.duiying(int(member))
        count = os_excel.search(title)
        aa.append(member)
        aa.append(title)
        aa.append(count)
        return render.lock(aa)

class home:
    def GET(self):
        return open('home.html',encoding = 'utf-8').read()

class jur:
    def POST(self):
        data = web.input()
        k = dict(data)
        number = k['question']
        if number == '1234qwer':
            kk = os_excel.look_all_title()
            cot = []
            for i in range(len(kk)):
                cot.append(kk[i])
            return render.jur(cot)
        else:
            return open('error.html', encoding='utf-8').read()

class jurs:
    def GET(self):
        kk = os_excel.look_all_title()
        cot = []
        for i in range(len(kk)):
            cot.append(kk[i])
        return render.jur(cot)

class result:
    def POST(self):
        data = web.input()
        k = dict(data)
        title = k['question']
        names = html.unescape(title)
        count = seek_similarity.count(names)
        title = os_excel.search_title(count)

        return render.result(title,count)


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
