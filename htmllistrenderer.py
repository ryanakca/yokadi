# -*- coding: UTF-8 -*-
"""
HTML rendering of t_list output

@author: Aurélien Gâteau <aurelien.gateau@free.fr>
@author: Sébastien Renard <sebastien.renard@digitalfox.org>
@license: GPLv3
"""
TASK_FIELDS = ["title", "creationDate", "dueDate", "doneDate", "description", "urgency", "status", "keywords"]

def printRow(out, tag, lst):
    print >>out, "<tr>"
    for value in lst:
        text = unicode(value).encode("utf-8") or "&nbsp;"
        print >>out, "<%s>%s</%s>" % (tag, text, tag)
    print >>out, "</tr>"

class HtmlListRenderer(object):
    def __init__(self, out):
        self.out = out

        #TODO: make this fancier
        print >>self.out, """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
                <html>
                <head>
                    <style>
                    td, th {
                        border: 1px solid #ccc;
                    }
                    </style>
                    <title>Yokadi tasks export</title>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                </head>
                <body>
                """

    def addTaskList(self, project, taskList):
        print >>self.out, (u"<h1>%s</h1>" % project.name).encode("utf-8")
        print >>self.out, "<table width='100%'>"
        printRow(self.out, "th", TASK_FIELDS)
        for task in taskList:
            lst = [getattr(task, field) for field in TASK_FIELDS if field!="keywords"]
            lst.append(task.getKeywordsAsString())
            printRow(self.out, "td", lst)
        print >>self.out, "</table>"

    def end(self):
        print >>self.out, "</body></html>"
# vi: ts=4 sw=4 et
