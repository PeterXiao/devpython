__author__ = 'Administrator'
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm import mapper
metadata = MetaData()
link = Table('atomisator_link',metadata,
             Column('id',Integer,primary_key=True),
             Column('url',String(300)),
             Column('atomisator_entry_id',Integer,
                    ForeignKey('atomisator_entry.id')))
class Link(object):
    def __init__(self,url):
        self.url = url
    def __repr__(self):
        return "<Link(%s)>" % self.url

mapper(Link,link)

tag = ('atomisator_link',metadata,
             Column('id',Integer,primary_key=True),
             Column('value',String(100)),
             Column('atomisator_entry_id',Integer,
                    ForeignKey('atomisator_entry.id')))
class Tag(object):
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return "<Link(%s)>" % self.value


mapper(Tag,tag)


class Entry(object):
    def __init__(self,title,url,summary,summary_detail='',title_detail=''):
        self.title = title
        self.url   = url
        self.summary = summary
        self.summary_detail = summary_detail
        self.title_detail =title_detail
    def add_links(self,links):
        for link in links:
            self.links.append(Link(link))
    def add_tag(self,tags):
        for tag in tags:
            self.tags.append(Tag(taag))
    def __repr__(self):
        return "<Entry(%r)>" % self.title
mapper(Entry,entry,property={
      'links':relationship(Link,backref('atomisator_entry')),
      'tags':relationship((Tag,backref('atomisator_entry')))
   })